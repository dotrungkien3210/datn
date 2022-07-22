import cv2
import streamlit as st
# code from https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv


def capture_image():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    #FRAME_WINDOW = st.image([])
    img_counter = 0
    take_img = st.button('Take an image')
    while True:
        ret, frame = cam.read()
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #FRAME_WINDOW.image(frame)
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)
        k = cv2.waitKey(1)
        if take_img:
            print("chay vao duoc roi 1")
            img_name = "test.jpg".format(img_counter)
            print("chay vao duoc roi 2")
            cv2.imwrite("data/" + img_name, frame)
            print("chay vao duoc roi 3")
            print("{} written!".format(img_name))
            print("chay vao duoc roi 4")
            cv2.destroyAllWindows()
            break
    cam.release()
    cv2.destroyAllWindows()

stop = st.button('stop')
if stop:
    cv2.destroyAllWindows()