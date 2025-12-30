import cv2 as cv



def rescaleFrame(frame, scale=0.75):
    # Works for images, videos and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(capture, width, height):
    # Only works for live video
    capture.set(3, width)
    capture.set(4, height)




# rescaled_img = rescaleFrame(img, scale=0.5)
# cv.imshow('Cat', img)
# cv.imshow('Resized Cat', rescaled_img)
# cv.waitKey(0)

capture = cv.VideoCapture('resources/videos/dog.mp4')


while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.5)
    if isTrue:
        cv.imshow('Video', frame)
        
        cv.imshow('Video Resized', frame_resized)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()