import cv2 as cv
import numpy as np

# Load an image from the specified file path
img = cv.imread("Resource/suresh.jpg")

# Resize the image to a new width (500) and height (700)
img = cv.resize(img, (500, 700))

# Create a resized version of the image for display purposes
img_resize = cv.resize(img, (750, 550))

# Convert the image to grayscale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2BGRA)

# Apply Gaussian blur to the image
blur_img = cv.GaussianBlur(img, (7, 7), 0)

# Apply Canny edge detection to the image
edge_img = cv.Canny(img, 47, 47)

# Create a 3x3 kernel for morphological operations
mat_kernel = np.ones((3, 3), np.uint8)

# Dilate the edges in the image
dilated_img = cv.dilate(edge_img, mat_kernel, iterations=1)

# Erode the dilated image
ero_img = cv.erode(dilated_img, mat_kernel, iterations=1)

# Print the shape (size) of the original image
print("the size of image:", img.shape)

# Crop a portion of the image (300x400 pixels) from the top-left corner
cropped_img = img[0:300, 0:400]

# Display various images using OpenCV
cv.imshow("original", img)
cv.imshow("cropped_img", cropped_img)
cv.imshow("resize", img_resize)
cv.imshow("gray", img_gray)
cv.imshow("blur", blur_img)
cv.imshow("edge", edge_img)
cv.imshow("dilated", dilated_img)
cv.imshow('erosion', ero_img)

# Wait until a key is pressed and then close all OpenCV windows
cv.waitKey(0)
cv.destroyAllWindows()
