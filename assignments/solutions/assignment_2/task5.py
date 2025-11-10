#Grayscale
import cv2
import numpy as np

def grayscale(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("grayscale.jpg", gray_image)
    print("grayscale.jpg saved")

if __name__ == '__main__':
    image = cv2.imread("lena.png")
    if image is None:
        print("No image")
    else:
        grayscale(image)