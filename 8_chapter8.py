import numpy as np  # Import the NumPy library, used for numerical operations
import cv2 as cv    # Import OpenCV library for image processing

# Create a black canvas with dimensions 600x600 using NumPy
img = np.zeros((600, 600))

# Create a white canvas with dimensions 600x600 using NumPy
img1 = np.ones((600, 600))

# Print the size (shape) of the black canvas
print("The Size of our canvas is:", img.shape)

# Create a colored canvas with dimensions 600x600 and 3 color channels (RGB)
color_img = np.zeros((600, 600, 3), np.uint8)

# Set a portion of the colored canvas to be a specific color
color_img[:] = 255, 0, 255
color_img[150:230, 100:500] = 255, 168, 10

# Draw a blue line from (0,0) to (300,300) with a thickness of 3 pixels
cv.line(color_img, (0, 0), (300, 300), (255, 0, 0), 3)

# Draw a blue line from (0,0) to the bottom right corner of the canvas
cv.line(color_img, (0, 0), (color_img.shape[0], color_img.shape[1]), (255, 0, 0), 3)

# Draw a rectangle with a top-left corner at (50,100) and bottom-right corner at (300,400) in orange
cv.rectangle(color_img, (50, 100), (300, 400), (255, 400, 0), 3)

# Draw a filled rectangle with the same dimensions and color
cv.rectangle(color_img, (50, 100), (300, 400), (255, 400, 0), cv.FILLED)

# Draw a filled circle with center at (400,300), radius 50, and color in orange
cv.circle(color_img, (400, 300), 50, (255, 100, 0), cv.FILLED)

# Draw an unfilled circle with the same parameters
cv.circle(color_img, (400, 300), 50, (255, 100, 0), 3)

# Put text "Suresh beekhani" at position (200,500) with a specified font, scale, color, and thickness
cv.putText(color_img, "Suresh beekhani", (200, 500), cv.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 1)


# Display the colored canvas in a window
cv.imshow("Colored", color_img)

# Wait indefinitely for a key press and then close all OpenCV windows
cv.waitKey(0)
cv.destroyAllWindows()


