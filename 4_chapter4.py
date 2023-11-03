import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

#Get the frame width and height for the output video
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
#cp.VideoWriter

while True:
    ret, Frame = cap.read()
    gray_Frame = cv.cvtColor(Frame, cv.COLOR_BGR2GRAY)
    
    # Apply a threshold to create a binary image
    (thresh, binary) = cv.threshold(gray_Frame, 100, 255, cv.THRESH_BINARY)

    cv.imshow('OriginalCam', Frame)
    cv.imshow('Graycam', gray_Frame)
    cv.imshow('Blackcam', binary)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
