import cv2 as cv

# Open the video file
cap = cv.VideoCapture('Resource/Video.mp4')

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error reading video")
    # You can add an exit statement here if needed

# Get the frame width and height for the output video
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Create a VideoWriter object to save the processed video
out = cv.VideoWriter('Resource/Out_video.mp4', cv.VideoWriter_fourcc('M',"J",'P','G'), 10, (frame_width, frame_height))

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if ret:
        # Convert the frame to grayscale
        grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Display the frame in a window named "Video"
        cv.imshow("Video", grayframe)

        # Write the frame to the output video
        out.write(frame)

        # Check if the 'q' key is pressed to exit the loop
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        # Break the loop if there are no more frames
        break

# Release the video capture and video writer objects
cap.release()
out.release()

# Close all OpenCV windows
cv.destroyAllWindows()
