import numpy as np
import serial
import cv2
import time;

# cap = cv2.VideoCapture('data/test_video_2.mp4')
cap = cv2.VideoCapture(2)

# color range
hsv_value = np.load('../data/hsv_value.npy')
lower_range = hsv_value[0]
upper_range = hsv_value[1]

# center of plate
center = np.load('../data/center.npy')

# ball countour area
max_area = 600
# arduino serial port
port = 'COM4'
serial_comm = serial.Serial(port, 115200, timeout = 1)

coordinates = "0,0>"

while (cap.isOpened()):
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_range, upper_range)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        # find the biggest countour (c) by the area
        c = max(contours, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        # print(cv2.contourArea(c))

        if cv2.contourArea(c) < max_area:
            # print('The ball is not on the plate \n')
            coordinates = "0,0>"
        else:
            # draw the biggest contour (c) in green
            # cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            
            # cv2.circle(frame, (cX, cY), 7, (255, 255, 255), -1)
            # cv2.line(frame, (cX, cY), (center[0], center[1]), (0, 255, 0), 2)
            # cv2.putText(frame, "center", (cX-20,cY-20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)

            coordinates = str(cX-center[0]) + ',' + str(center[1]-cY) + '>'
    # cv2.imshow('Original video', frame)
    # # cv2.imshow('Mask detection', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    print(coordinates)
    serial_comm.write(coordinates.encode())

serial_comm.close()
cap.release()
cv2.destroyAllWindows()
