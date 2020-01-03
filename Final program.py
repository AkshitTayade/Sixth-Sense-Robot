import cv2
import numpy as np 
import serial
import time

#create serial port object called arduino Serial data
Arduino = serial.Serial('/dev/cu.usbmodem14101',9600)

#wait for 2 second for the communication to get established
time.sleep(2)


cam = cv2.VideoCapture(0)

#for detecting yellow coloured ball
lower_yellow = np.array([20,100,100])
upper_yellow = np.array([40,255,255])


while(cam.isOpened()) :
    ret,frame = cam.read()
    frame = cv2.flip(frame,1)

    w = frame.shape[1]
    h = frame.shape[0]

    #smoothen the image
    img_smooth = cv2.GaussianBlur(frame,(7,7),0)

    #define ROI
    mask = np.zeros_like(frame)
    mask[100:550, 100:550]  = [255,255,255]

    image_roi = cv2.bitwise_and(img_smooth, mask)
    
    #creating 3x3 matrix to move ball
    cv2.rectangle(frame,(100,100),(550,550),(0,0,255),2)
    cv2.line(frame,(250,100),(250,550),(0,0,255),2)
    cv2.line(frame,(400,100),(400,550),(0,0,255),2)
    cv2.line(frame,(100,250),(550,250),(0,0,255),2)
    cv2.line(frame,(100,400),(550,400),(0,0,255),2)


    #Threshold the image for yellow color
    img_hsv = cv2.cvtColor(image_roi,cv2.COLOR_BGR2HSV)

    img_thresh = cv2.inRange(img_hsv,lower_yellow,upper_yellow)
    
    #find contours 
    contours,heirachy = cv2.findContours(img_thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    #find the index of largest contours
    if(len(contours)!=0) :
        areas = [cv2.contourArea(c) for c in contours]
        max_index = np.argmax(areas)
        cnt = contours[max_index]
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
        #pointer on Video
        M= cv2.moments(cnt)
        if(M['m00']!=0) :
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(frame,(cx,cy),4,(0,255,0),-1)

        #trace the cursor motion
        if cx in range(250,400) :
            if cy < 250 :
                print("Upper Middle")
                Arduino.write(b'f')

            elif cy > 400 :
                print("Lower Middle")
                Arduino.write(b'b')

            else :
                print("Center")
                Arduino.write(B's')

        if cy in range(250,400) :
            if cx < 250 :
                print("Left Middle")
                Arduino.write(b'l')

            elif cx > 400 :
                print("Right Middle")
                Arduino.write(b'r')

            else :
                print("Center")
                Arduino.write(b's')
            
    cv2.imshow('Frame',frame)

    key = cv2.waitKey(10)
    if key ==27 :
        break


cam.release()
cv2.destroyAllWindows()