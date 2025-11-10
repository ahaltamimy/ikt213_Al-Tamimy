#resize
import cv2

def resize(image,width,height):
    resized_image = cv2.resize(image,(width,height))
    cv2.imwrite('resized_image.jpg',resized_image)
    print("resized_image.jpg saved")

if __name__ == '__main__':
    image = cv2.imread("lena.png")
    if image is None:
        print("No image")
    else:
        resize(image,200,200)