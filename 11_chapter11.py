import cv2 as cv 
import numpy as np 

img =cv.imread('Resource\suresh.jpg')

hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Display the vertically stacked image in a window titled "Vertical"
cv.imshow("Orginal", img)
cv.imshow("HSV", hsv_img)

# Wait indefinitely until a key is pressed and then close all windows
cv.waitKey(0)
cv.destroyAllWindows()
