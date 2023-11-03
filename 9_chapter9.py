# Import the necessary libraries
import cv2 as cv
import numpy as np

# Open the default camera (camera index 0)
cap = cv.VideoCapture(0)

# Function to set the camera resolution to HD (1280x720)
def hd_resolution():
    cap.set(3, 1280)  # Set width to 1280 pixels
    cap.set(4, 720)   # Set height to 720 pixels

# Call the function to set HD resolution
hd_resolution()

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if the frame was successfully captured
    if not ret:
        break

    # Display the captured frame in a window named "Camera"
    cv.imshow("Camera", frame)

    # Check for the 'q' key to exit the loop
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and destroy all OpenCV windows
cap.release()
cv.destroyAllWindows()
