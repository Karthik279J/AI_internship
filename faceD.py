    #haarcascade
        #this is a .xml file and ML based object detection method by opencv, 
        #it works by suing haar - like features(edges, lines, rectangles)
        #trained with +ve and -ve images using cascade calssifier for rejections works on CPU
    import cv2
    face_cascade=cv2.CascadeClassifier("Data\haarcascade_frontalface_default.xml")
    img=cv2.imread(r'img\trump.jpeg')
    GRAY=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(GRAY, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for(x,y,w,h)in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("IMG",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
