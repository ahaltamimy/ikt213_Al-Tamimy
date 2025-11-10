import cv2
import numpy as np



# template_match


def template_match(image, template):
    # Ensure both are grayscale (handle if already gray)
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
    templ_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY) if len(template.shape) == 3 else template

    # Template matching (normalized correlation)
    res = cv2.matchTemplate(img_gray, templ_gray, cv2.TM_CCOEFF_NORMED)

    threshold = 0.9
    loc = np.where(res >= threshold)

    h, w = templ_gray.shape
    out = image.copy()

    for pt in zip(*loc[::-1]):  # (x, y)
        top_left = pt
        bottom_right = (pt[0] + w, pt[1] + h)
        cv2.rectangle(out, top_left, bottom_right, (0, 0, 255), 2)

    cv2.imwrite("template_matched.jpg", out)
    print("saved template_matched.jpg")
    return out


if __name__ == "__main__":
    # Read in color; function converts to gray internally (per tutorial)
    img = cv2.imread("shapes-1.png")
    templ = cv2.imread("shapes_template.jpg")
    if img is None or templ is None:
        print("can't load image or template")
    else:
        template_match(img, templ)
