#RGB to use HSV
import cv2

def hsv(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imwrite("hsv.png", hsv_image)
    print("hsv image is saved")

if __name__ == "__main__":
    image = cv2.imread("lena.png")
    if image is None:
        print("No image")
    else:
        hsv(image)
