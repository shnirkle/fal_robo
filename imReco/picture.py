"""

This file provides necessary functions to capture images.

"""

import cv2 as cv

CAMID = 2  # Device ID of the camera. Default is 0

cam = cv.VideoCapture(CAMID, cv.CAP_ANY)

"""
captures an Image with the connected camera.
should be enough to just capture the default camera, since only one will be connected to the raspberry pi
"""

def capImage() -> object or bool:

    if not cam.isOpened():
        # check if camera can be opened
        print("Unable to open camera with id: ", CAMID)
        return False

    ret, frame = cam.read()  # read a frame from the camera

    if ret is False:
        # check the status of the image capture
        print("Unable to capture Imagae. Return status: ", ret)
        return False

    return frame


if __name__ == "__main__":
    # code will only be executed if run directly.
    frame = capImage()
    cv.imwrite("test.png", frame)
