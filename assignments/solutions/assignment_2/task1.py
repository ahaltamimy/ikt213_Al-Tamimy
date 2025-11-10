#padding
import cv2

def padding(img, border_width):

    padded_image= cv2.copyMakeBorder(
    img
    , border_width
    , border_width
    , border_width
    , border_width
    , borderType=cv2.BORDER_REFLECT
    )

    cv2.imwrite('padded_image.jpg', padded_image)
    print("Image saved as 'padded_image.jpg'.")

if __name__ == "__main__":
    image = cv2.imread("lena.png")
    if image is None:
        print("Could not load image.")
    else:
        padding(image, border_width=100)