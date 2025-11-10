#smoothing
from email.mime import image

import cv2

def smoothing(image):
    smoothed_image = cv2.GaussianBlur(image, (15, 15), 0, borderType=cv2.BORDER_DEFAULT)
    cv2.imwrite("smoothed_image.jpg", smoothed_image)
    print("smoothed_image.jpg")

if __name__ == "__main__":
    image = cv2.imread("lena.png")
    if image is None:
        print("No image")
    else:
        smoothing(image)
