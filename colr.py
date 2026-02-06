import cv2
import numpy as np
cam=cv2.VideoCapture(0)
while True:
    ret, frame=cam.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_blue=np.array([0, 30, 60])
    upper_blue=np.array([30, 150, 255])
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    result=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('win',result)
    #cv2.createTrackbar('name','trak_bar',150,255,3)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cam.release()
