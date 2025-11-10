import cv2
import numpy as np

#canny_edge

def canny_edge_detection(image, threshold_1, threshold_2):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    edges = cv2.Canny(blurred, threshold_1, threshold_2)

    cv2.imwrite("canny_edges.jpg", edges)
    print("saved canny_edges.jpg")

if __name__ == "__main__":
    img = cv2.imread("lambo.png")
    if img is None:
        print("no image")
    else:
        canny_edge_detection(img, 50,50)
