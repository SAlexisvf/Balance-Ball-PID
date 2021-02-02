import numpy as np
import imutils
import cv2

cap = cv2.VideoCapture('data/test_video_2.mp4')

# color range
lower_range = np.array([117, 0, 216])
upper_range = np.array([179, 255, 255])

# ball countour area
max_area = 6000

while(cap.isOpened()):
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_range, upper_range)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        # draw in blue the contours that were founded
        # cv2.drawContours(frame, contours, -1, 255, 3)

        # find the biggest countour (c) by the area
        c = max(contours, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)

        if cv2.contourArea(c) < max_area:
            print('The ball is not on the plate \n')
        
        else:
            # draw the biggest contour (c) in green
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            
            cv2.circle(frame, (cX, cY), 7, (255, 255, 255), -1)
            cv2.putText(frame, "center", (cX-20,cY-20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)

            print('cX: ', cX)
            print('cY: ', cY, '\n')

    cv2.imshow('Original video', frame)
    # cv2.imshow('Mask detection', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()