import cv2

def save_camera_information(filename="camera_outputs.txt"):

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam")
        return


    fps = cap.get(cv2.CAP_PROP_FPS)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)


    cap.release()


    with open(filename, "w") as f:
        f.write(f"fps: {fps}\n")
        f.write(f"height: {height}\n")
        f.write(f"width: {width}\n")

    print(f"Camera information saved to {filename}")


def main():
    save_camera_information("camera_outputs.txt")


if __name__ == "__main__":
    main()
