# Import the OpenCV library and NumPy
import cv2 as cv
import numpy as np
from cv2 import cvtColor, imwrite

# Load an image from the specified file path
img = cv.imread("Resource\suresh.jpg")

# Resize the image to the desired dimensions (800x600)
img = cv.resize(img, (800, 600))

# Convert the resized image to grayscale
gray = cvtColor(img, cv.COLOR_BGR2GRAY)

# Apply a threshold to create a binary image
(thresh, binary) = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)

# Display the original image in a window with the title "original"
cv.imshow("original", img)

# Display the grayscale image in a window with the title "Gray Image"
cv.imshow("Gray Image", gray)

# Display the binary image in a window with the title "Black and White Image"
cv.imshow("Black and White", binary)

# Save the grayscale image to a file
#imwrite('Resource/suresh_gray.jpg', gray)

# Wait indefinitely for a key press and close the window on key press (commented out for now)
cv.waitKey(0)

# Close all OpenCV windows (commented out for now)
cv.destroyAllWindows()
