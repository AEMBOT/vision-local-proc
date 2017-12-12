



import numpy as np
import cv2
from greenCross import GripGreenCross
cap = cv2.VideoCapture(1)
cap.set(cv2.cv.CV_CAP_PROP_FPS, 60)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,640);
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,480);
green = GripGreenCross()
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    green.process(frame)
    mask = green.mask_output
    
    contour = green.filter_contours_output

    # Our operations on the frame come here


    # Display the resulting frame
    cv2.drawContours(mask,	 contour,-1,(0,0,255),3) 
    cv2.imshow('mask', mask)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
