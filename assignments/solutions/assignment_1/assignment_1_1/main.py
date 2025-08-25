import cv2



def print_image_information(image):

    height, width, channels = image.shape

    print("Height:", height)
    print("Width:", width)
    print("Channels:", channels)
    print("Size:", image.size)
    print("Data type:", image.dtype)


def main():

    image = cv2.imread("lena-1.png")

    if image is None:
        print("Error: Could not load image. Make sure 'lena-1.png' is in the project folder.")
        return


    print_image_information(image)


if __name__ == "__main__":
    main()
