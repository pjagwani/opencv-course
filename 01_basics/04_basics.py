import cv2 as cv

img = cv.imread('resources/photos/park.jpg')
cv.namedWindow('Park', cv.WINDOW_NORMAL)
cv.imshow('Park', img)
cv.moveWindow('Park', 0, 0)

# #make a grayscale image
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.namedWindow('Gray', cv.WINDOW_NORMAL)
# cv.imshow('Gray', gray)
# cv.moveWindow('Gray', 800, 0)


#Blur image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.namedWindow('Blur', cv.WINDOW_NORMAL)
cv.imshow('Blur', blur)
cv.moveWindow('Blur', 0, 600)



# cascade edge
canny = cv.Canny(blur, 125, 175)
cv.namedWindow('Canny', cv.WINDOW_NORMAL)
cv.imshow('Canny', canny)
cv.moveWindow('Canny', 800, 600)

#Dilate the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)
cv.moveWindow('Dilated', 800, 0)

#erode
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)
cv.moveWindow('Eroded', 0, 0)

#resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)
cv.moveWindow('Resized', 400, 0)

#cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)
cv.moveWindow('Cropped', 400, 600)
cv.waitKey(0)