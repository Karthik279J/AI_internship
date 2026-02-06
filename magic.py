import cv2
import numpy as np
import time
cam=cv2.VideoCapture(0)
time.sleep(3)
for i in range(30):
    ret,background=cam.read()
while True:
    ret,frame=cam.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_blue1=np.array([0, 30, 60])
    upper_blue1=np.array([30, 150, 255])
    mask1=cv2.inRange(hsv,lower_blue1,upper_blue1)
    lower_blue2=np.array([0, 30, 60])
    upper_blue2=np.array([30, 150, 255])
    mask2=cv2.inRange(hsv,lower_blue2,upper_blue2)
    mask=mask1+mask2
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    result=cv2.bitwise_and(background,background,mask=mask)
    body=cv2.bitwise_and(frame,frame,mask=cv2.bitwise_not(mask))
    final_result=cv2.add(result,body)
    cv2.imshow('win',final_result)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cam.release()
    
