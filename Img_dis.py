import cv2

img1 = cv2.imread('img\car.jpeg',0)
cv2.imshow("name1",img1)
cv2.waitKey(10)
img1 = cv2.imread('img\car.jpeg',-1)
cv2.imshow("name1",img1)
cv2.waitKey(10)
cv2.destroyAllWindows()
