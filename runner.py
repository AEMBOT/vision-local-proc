import numpy as np
import cv2
from greenCross import GripGreenCross
from reflectiveTape import ReflectivePipeline

#camera settings
#-1 finds the first camera, so ensure only 1 camera is in
cap = cv2.VideoCapture(1)
cap.set(cv2.cv.CV_CAP_PROP_FPS, 60)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,640);
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,480);

#pipeline processor object
og = ReflectivePipeline()

while(True):
    # Pass in frame from camera (cap)
    _, frame = cap.read()
    og.process(frame)
    
    #set mask and countour frames
    mask = og.mask_output
    contour = og.filter_contours_output
    if len(contour) > 0:
		cnt = contour[0]
		#rectangle approximation code (opencv 3.0+ code)
		#rect = cv2.minAreaRect(cnt)
		#box = cv2.boxPoints(rect)
		#box = np.int0(box)
		#cv2.drawContours(frame, [box], 0, (0,0,255), 2)
    
    
    
	#show countour on mask
    cv2.drawContours(mask,	 contour,-1,(0,0,255),3) 
    
	#show frames mask and default frame
    cv2.imshow('mask', mask)
    cv2.imshow('frame',frame)
    
    #check if q is hit to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
