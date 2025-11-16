import cv2
import numpy as np


def align_images(image_to_align, reference_image, max_features, good_match_precent):


    img_align_color = cv2.imread(image_to_align)
    img_ref_color = cv2.imread(reference_image)

    if img_align_color is None or img_ref_color is None:
        raise IOError("Could not read input images. Check the file paths.")

    img_align_gray = cv2.cvtColor(img_align_color, cv2.COLOR_BGR2GRAY)
    img_ref_gray = cv2.cvtColor(img_ref_color, cv2.COLOR_BGR2GRAY)

    # detect SIFT keypoints and descriptors, no limit as of now, use limit later
    sift = cv2.SIFT_create()
    kp_ref, des_ref = sift.detectAndCompute(img_ref_gray, None)
    kp_align, des_align = sift.detectAndCompute(img_align_gray, None)

    if des_ref is None or des_align is None:
        raise ValueError("No SIFT features found in one of the images.")

    # set up flann parms
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    knn_matches = flann.knnMatch(des_ref, des_align, k=2)

    # lowe's ratio test
    good_matches = []
    for m, n in knn_matches:
        if m.distance < good_match_precent * n.distance:
            good_matches.append(m)

    # sorts the matches by distance, sorts it by best first
    good_matches = sorted(good_matches, key=lambda x: x.distance)


    MIN_MATCH_COUNT = 4
    if len(good_matches) < MIN_MATCH_COUNT:
        print(
            f"Not enough good matches are found - "
            f"{len(good_matches)}/{MIN_MATCH_COUNT}"
        )
        # still create a matches image so the script produces outputs
        matches_img = cv2.drawMatches(
            img_ref_color, kp_ref,
            img_align_color, kp_align,
            good_matches[:max_features], None,
            matchColor=(0, 255, 0),
            flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS,
        )
        cv2.imwrite("aligned.png", img_align_color)
        cv2.imwrite("matches.png", matches_img)
        return img_align_color, matches_img, None

    # compute homography with all good matches
    src_pts = np.float32(
        [kp_ref[m.queryIdx].pt for m in good_matches]
    ).reshape(-1, 1, 2)
    dst_pts = np.float32(
        [kp_align[m.trainIdx].pt for m in good_matches]
    ).reshape(-1, 1, 2)

    H, mask = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC, 5.0)

    # warp image_to_align to reference_image with extra padding
    h, w, _ = img_ref_color.shape

    # add some extra vertical space at the bottom so the last line is shown
    out_h = int(h * 1.05)  # 5% extra

    aligned = cv2.warpPerspective(img_align_color, H, (w, out_h))

    # build a clean matches image

    # mask: 1 = inlier, 0 = outlier
    mask = mask.ravel().tolist()

    # keep only inlier matches
    inlier_matches = [m for m, inlier in zip(good_matches, mask) if inlier]

    # sort inliers and keep only the best max_features
    inlier_matches = sorted(inlier_matches, key=lambda x: x.distance)[:max_features]

    # matchesMask for drawMatches must have same length as inlier_matches
    matchesMask_vis = [1] * len(inlier_matches)

    draw_params = dict(
        matchColor=(128, 128, 0),
        singlePointColor=None,   # draws only matched keypoints
        matchesMask=matchesMask_vis,
        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS,
    )

    matches_img = cv2.drawMatches(
        img_ref_color,  kp_ref,
        img_align_color, kp_align,
        inlier_matches, None,
        **draw_params,
    )

    cv2.imwrite("aligned.png", aligned)
    cv2.imwrite("matches.png", matches_img)

    return aligned, matches_img, H


if __name__ == "__main__":
    # Call with the exact parameters the lab specifies for SIFT/FLANN:
    align_images(
        image_to_align="align_this.jpg",
        reference_image="reference_img.png",
        max_features=10,
        good_match_precent=0.7,
    )
