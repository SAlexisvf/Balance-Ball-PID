#finding hsv range of target object(pen)
import cv2
import numpy as np
import time
# A required callback method that goes into the trackbar function.
def nothing(x):
    pass

# Initializing the webcam feed.
cap = cv2.VideoCapture(2)
# cap = cv2.imread("data/test_image_1.jpeg")
cap.set(3,1280)
cap.set(4,720)

def mouseHSV(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        global colors
        colors = hsv[y,x]
        print("HSV Format: ", colors)
        print("Coordinates of pixel: X: ",x,"Y: ",y)

# Create a window named trackbars.
cv2.namedWindow("Trackbars")
cv2.namedWindow("Original")
cv2.namedWindow("Filter")

# Create mouse callback
cv2.setMouseCallback('Original', mouseHSV)

# Now create 6 trackbars that will control the lower and upper range of 
# H,S and V channels. The Arguments are like this: Name of trackbar, 
# window name, range,callback function. For Hue the range is 0-179 and
# for S,V its 0-255.
cv2.createTrackbar("H", "Trackbars", 0, 100, nothing)
cv2.createTrackbar("S", "Trackbars", 0, 100, nothing)
cv2.createTrackbar("V", "Trackbars", 0, 100, nothing)

colors = [0, 0, 0]
 
while True:
    # Start reading the webcam feed frame by frame.
    ret, origina_frame = cap.read()
    if not ret:
        break

    #percent by which the image is resized
    scale_percent = 50

    #calculate the 50 percent of original dimensions
    width = int(origina_frame.shape[1] * scale_percent / 100)
    height = int(origina_frame.shape[0] * scale_percent / 100)

    frame = cv2.resize(origina_frame, (width, height))

    # Flip the frame horizontally (Not required)
    frame = cv2.flip( frame, 1 ) 
    
    # Convert the BGR image to HSV image.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Get the new epsilon values of the trackbar in real time as the user changes 
    # them
    h_epsilon = cv2.getTrackbarPos("H", "Trackbars")
    s_epsilon = cv2.getTrackbarPos("S", "Trackbars")
    v_epsilon = cv2.getTrackbarPos("V", "Trackbars")
 
    # Set the lower and upper HSV range according to the value selected
    # by the trackbar
    lower_range = np.array([max(0, colors[0]*(1-h_epsilon*3/100)), max(0, colors[1]*(1-s_epsilon*3/100)), max(0, colors[2]*(1-v_epsilon*3/100))]).astype(int)
    upper_range = np.array([min(colors[0]*(1+h_epsilon*3/100), 179), min(colors[1]*(1+s_epsilon*3/100), 255), min(colors[2]*(1+v_epsilon*3/100), 255)]).astype(int)

    print(lower_range)
    print(upper_range)
    
    # Filter the image and get the binary mask, where white represents 
    # your target color
    mask = cv2.inRange(hsv, lower_range, upper_range)
 
    # # You can also visualize the real part of the target color (Optional)
    # res = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Converting the binary mask to 3 channel image, this is just so 
    # we can stack it with the others
    mask_3 = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    
    # # stack the mask, orginal frame and the filtered result
    # stacked = np.hstack((mask_3,res))
    
    # Show this stacked frame at 40% of the size.
    # cv2.imshow('Trackbars', )
    cv2.imshow('Original', frame)
    cv2.imshow('Filter', cv2.resize(mask_3, None, fx=0.4, fy=0.4))
    
    # If the user presses ESC then exit the program
    key = cv2.waitKey(1)
    if key == 27:
        break
    
    # If the user presses `s` then print this array.
    if key == ord('s'):
        thearray = [lower_range, upper_range]
        print(thearray)
        # Also save this array as penval.npy
        np.save('hsv_value', thearray)
    
# Release the camera & destroy the windows.    
cap.release()
cv2.destroyAllWindows()