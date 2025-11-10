#shift rgb
from email.mime import image

import cv2
import numpy as np

def hue_shifted(image, emptyPictureArray, hue):

    shifted = image.astype(np.int16) + int(hue)
    shifted = np.clip(shifted, 0, 255).astype(np.uint8)
    emptyPictureArray[:] = shifted

    cv2.imwrite("hue_shifted.jpg", emptyPictureArray)
    print("hue_shifted image is saved")

if __name__ == "__main__":
    image = cv2.imread("lena.png")
    if image is None:
        print("No image")
    else:
        h, w, _ = image.shape
        emptyPictureArray = np.zeros((h, w, 3), dtype=np.uint8)
        hue_shifted(image, emptyPictureArray, 50)
