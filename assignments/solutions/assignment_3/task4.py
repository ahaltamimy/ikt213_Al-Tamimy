import cv2
import numpy as np

#resize

def resize(image, scale_factor: int, up_or_down: str):
    if scale_factor < 1:
        raise ValueError("scale factor must be an integer greater or equal to 1")

    out = image.copy()

    if up_or_down.lower() == "up":
        for _ in range(scale_factor):
            out = cv2.pyrUp(out)  # doubles size each step

    elif up_or_down.lower() == "down":
        for _ in range(scale_factor):
            out = cv2.pyrDown(out) # halves size each step

    else:
        raise ValueError("up_or_down must be either 'up' or 'down'")

    return out



if __name__ == "__main__":
    img = cv2.imread("lambo.png")
    if img is None:
        print("can't load image")
    else:
        # 2x zoom in
        zoom_in = resize(img, 2, "up")
        cv2.imwrite("lambo_zoom_in.jpg", zoom_in)

        # 2x zoom out
        zoom_out = resize(img, 2, "down")
        cv2.imwrite("lambo_zoom_out.jpg", zoom_out)

        print("lambo_zoom_in.jpg and lambo_zoom_out.jpg saved")