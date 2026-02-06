import cv2
import numpy as np
cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    bx, by, bw, bh = 200, 150, 200, 200
    cv2.rectangle(frame, (bx, by), (bx + bw, by + bh), (255, 255, 255), 2)
    roi = hsv[by:by+bh, bx:bx+bw]
    # Storing colors in a list [Name, Lower, Upper]
    data = [
        ["Blue",   [100, 150, 50], [140, 255, 255]],
        ["Green",  [40, 50, 50],   [80, 255, 255]],
        ["Red",    [0, 150, 50],   [10, 255, 255]],
        ["Yellow", [25, 150, 50],  [35, 255, 255]],
        ["Orange", [11, 150, 50],  [24, 255, 255]],
        ["White",  [0, 0, 150],    [180, 50, 255]]
    ]
    color = "None"
    for name, low, upp in data:
        mask = cv2.inRange(roi, np.array(low), np.array(upp))
        if np.sum(mask) > 200000:
            color = name
            break 
    cv2.putText(frame, color, (bx, by-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('win', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
