import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier('./Hardware_Access/Cascades/haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('./Hardware_Access/Cascades/haarcascade_eye.xml')

cap = cv2.VideoCapture('http://192.168.0.231:81/stream')
cap.set(3,1280)
cap.set(4,720)
  
while True:
    ret, img = cap.read()
    #cv2.imwrite('sample.jpg',img)
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     

    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]  
    
        eyes = eyeCascade.detectMultiScale(
                roi_gray,
                scaleFactor= 1.5,
                minNeighbors=10,
                minSize=(5, 5),
                )
        
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()