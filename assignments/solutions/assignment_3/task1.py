import cv2
import numpy as np

#Sobel edge

def sobel_edge_detection(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blured = cv2.GaussianBlur(gray, (3, 3), 0)
    sobel = cv2.Sobel(blured, cv2.CV_64F, 1, 1, ksize=1)
    sobel_abs = cv2.convertScaleAbs(sobel)

    cv2.imwrite("sobel_edges.jpg", sobel_abs)
    print("saved sobel_edges.jpg")

if __name__ == "__main__":
    img = cv2.imread("lambo.png")
    if img is None:
        print("can't load image")
    else:
        sobel_edge_detection(img)

