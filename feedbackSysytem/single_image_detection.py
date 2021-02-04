import cv2
import numpy as np

img = cv2.imread('../data/test_image_1.jpeg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# color range
lower_range = np.array([0,70,50])
upper_range = np.array([10,255,255])

mask = cv2.inRange(hsv, lower_range, upper_range)

if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.destroyAllWindows()

cv2.imshow('Image', img)
cv2.imshow('Mask', mask)

cv2.waitKey(0)
cv2.destroyAllWindows()