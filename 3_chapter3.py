import cv2 as cv
import numpy as np 
from tkinter import Frame

cap = cv.VideoCapture(0)

while (cap.isOpened()):  # Changed to while loop syntax
    ret, frame = cap.read()  # Changed 'framem' to 'frame'
    if ret:
        cv.imshow("Frame", frame)  # Changed 'cv.show' to 'cv.imshow' and 'Frame' to 'frame'
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture object
cap.release()

# Close all OpenCV windows
cv.destroyAllWindows()
