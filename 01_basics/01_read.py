import cv2 as cv

#img = cv.imread('resources/photos/cat_large.jpg')
#cv.imshow('Cat', img)
#cv.waitKey(0)

capture = cv.VideoCapture('resources/videos/kitten.mp4')

while True:
    isTrue, frame = capture.read()
    
    if isTrue:
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()

