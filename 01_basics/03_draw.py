import cv2 as cv
import numpy as np

blank_image = np.zeros((512, 512,3), dtype='uint8')
#cv.imshow('Blank', blank_image)

# #Paint the image a certain color
# blank_image[:] = 0, 255, 0
# cv.imshow('Green', blank_image)


#blank_image[200:300, 300:400] = 0, 0, 255
#cv.imshow('Red', blank_image)


#Draw a rectangle
cv.rectangle(blank_image, (0,0), (blank_image.shape[1]//2, blank_image.shape[0]//2), (0,255,0), thickness=-1)
#cv.imshow('Rectangle', blank_image)

#Draw a circle
cv.circle(blank_image, (blank_image.shape[1]//2, blank_image.shape[0]//2), 40, (255,0,0), thickness=3)
#cv.imshow('Circle', blank_image)

cv.line(blank_image, (0,0), (blank_image.shape[1]//2, blank_image.shape[0]//2), (255,255,255), thickness=6)

cv.putText(blank_image, 'Hello', (225,225), cv.FONT_ITALIC, 1.0, (0,0,255), thickness=2)
cv.imshow('Line', blank_image)
cv.waitKey(0)