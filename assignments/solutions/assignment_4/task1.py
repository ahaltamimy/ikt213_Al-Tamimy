import cv2
import numpy as np


def harris(reference_image):

    gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    dst = cv2.cornerHarris(gray, 2, 3, 0.04)
    dst = cv2.dilate(dst, None)

    result_image = reference_image.copy()
    result_image[dst > 0.01 * dst.max()] = [0, 0, 255]

    cv2.imwrite("harris.jpg", result_image)

if __name__ == "__main__":
    image = cv2.imread("reference_img.png")
    harris(image)

