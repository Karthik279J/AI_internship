import cv2
import os
face_cascade = cv2.CascadeClassifier('Data/haarcascade_frontalface_default.xml')
user_id = input('Enter User ID: ')
save_path = f'dataset/user_{user_id}'
if not os.path.exists(save_path):
    os.makedirs(save_path)
cam = cv2.VideoCapture(0)
count = 0
print("Starting capture. Look at the camera...")
while True:
    ret, frame = cam.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5,minSize=(30,30))
    for (x, y, w, h) in faces:
        count += 1
        # Crop and resize the face
        face_img = gray[y:y+h, x:x+w]
        face_img = cv2.resize(face_img, (150, 150))
        cv2.imwrite(f"{save_path}/{count}.jpg", face_img)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow("Capturing Faces - Press 'q' to quit", frame)
    if cv2.waitKey(1) & 0xFF == ord('q') or count >= 50:
        break
print(f"Successfully saved {count} images to {save_path}")
cam.release()
cv2.destroyAllWindows()
