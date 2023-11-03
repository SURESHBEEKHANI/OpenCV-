import cv2 as cv
import numpy as np

# Open a video capture object for the default camera (usually 0)
cap = cv.VideoCapture(0)

# Set the brightness to 100 (adjust this value as needed)
cap.set(10, 100)

# Set the width of the frame to 640 pixels
cap.set(3, 640)

# Set the height of the frame to 480 pixels
cap.set(4, 480)

while True:
    ret, frame = cap.read()

    if ret:
        cv.imshow("frame", frame)

        # Break the loop if the 'q' key is pressed
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

# Release the video capture object and close the OpenCV windows
cap.release()
cv.destroyAllWindows()
