# Import the OpenCV library and NumPy
import cv2 as cv
import numpy as np

# Read an image named "suresh.jpg" from the "Resource" directory
img = cv.imread("Resource\suresh.jpg")

# Create a horizontally stacked image by concatenating the 'img' twice
hor_img = np.hstack((img, img))

# Create a vertically stacked image by concatenating the 'img' twice
var_img = np.vstack((img, img))

# Display the horizontally stacked image in a window titled "Horizontal"
cv.imshow("Horizontal", hor_img)

# Display the vertically stacked image in a window titled "Vertical"
cv.imshow("Vertical", var_img)

# Wait indefinitely until a key is pressed and then close all windows
cv.waitKey(0)
cv.destroyAllWindows()
