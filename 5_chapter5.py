import cv2 as cv
import numpy as np

# Open a video capture object for the default camera (camera index 0)
cap = cv.VideoCapture(0)

# Get the frame width and height for the output video
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the output video writer
out = cv.VideoWriter('Resource/Out_video.mp4', cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width  , frame_height))

while True:
    # Read a frame from the video capture
    (ret, frame) = cap.read()
    
    if ret:  # Check if the frame was read successfully
        # Write the frame to the output video
        out.write(frame)

        # Display the original frame in a window named 'OriginalCam'
        cv.imshow('Video', frame)

        # Check for the 'q' key press to exit the loop
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

# Release the video capture and video writer objects
cap.release()
out.release()

# Close all OpenCV windows
cv.destroyAllWindows()
