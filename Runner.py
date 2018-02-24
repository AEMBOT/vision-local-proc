from networktables import NetworkTables
from grip import GripPipeline
import cv2
import numpy as np

# camera settings
# -1 finds the first camera, so ensure only 1 camera is in
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FPS, 60)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640);
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480);

ip = '10.64.43.2'
NetworkTables.initialize(ip)
table = NetworkTables.getTable('SmartDashboard')

# pipeline processor object
pipeline = GripPipeline()

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    #pipeline processes through everything determining boxes and masks etc
    pipeline.process(frame)

    # set mask and countour frames
    mask = pipeline.mask_output
    contour = pipeline.filter_contours_output
    if len(contour) > 0:
        cnt = contour[0]
        # rectangle approximation code (opencv 3.0+ code)
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)
        print(box)
        #cause I want the origin at the bottom left, references top left of cube
        table.putNumber("XLocation",box[0][0])

    # show countour on mask
    cv2.drawContours(mask, contour, -1, (0, 0, 255), 3)

    # show frames mask and default frame
    cv2.imshow('mask', mask)

    cv2.imshow('frame', frame)

    # check if q is hit to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    print("t")

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()