import cv2
import numpy as np
from pipeline.powerCubeV2 import GripPipeline

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 60)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

pipeline = GripPipeline()

while(True):
    ret, frame = cap.read()

    cv2.imshow('frame', frame)

    pipeline.process(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    # set mask and countour frames
    mask = pipeline.mask_output
    contour = pipeline.filter_contours_output
    if len(contour) > 0:
        cnt = contour[0]
        # rectangle approximation code (opencv 3.0+ code)
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(ret, [box], 0, (0,0,255), 2)

        # show countour on mask
        cv2.drawContours(mask, contour, -1, (0, 0, 255), 3)

    cv2.imshow("mask", mask)
cap.release()
cv2.destroyAllWindows()