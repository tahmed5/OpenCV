import numpy as np
import cv2
import pickle
import random

want = str(input('DO YOU WANT?\n'))
user = None

if want.lower() == 'y':
    user = str(input('Who Are You?\n'))
    

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

with open("labels.pickle", 'rb') as f: #wb = writing bytes
    labels = pickle.load(f)
    labels = {v:k for k,v in labels.items()}

print(labels)
cap = cv2.VideoCapture(2)

while True:
    ret, frame = cap.read()
    retval, wframe = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, scaleFactor = 1.5, minNeighbors = 5)
    
    for (x, y, w, h) in faces: #region of interest = x,y,w,h
        roi_grey = grey[y:y+h, x:x+w] #returns all the pixels from x,y plus the width and height selecting a specfic region
        roi_frame = frame[y:y+h, x:x+w]

        # recogniser - deep learned model
        id_, conf = recognizer.predict(roi_grey)
        if conf >= 45:
            #print(id_)
            #print(labels[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            colour = (255,255,255)
            stroke = 2
            cv2.putText(frame,name,(x,y), font, 1, colour,stroke,cv2.LINE_AA)
            print(name)

        key = cv2.waitKey(19)

        if key == ord(' ') and user != None:
            rint = random.randint(0, 9999999)
            cv2.imwrite('./images/{}/{}.jpg'.format(user,rint), wframe)

        #img_item = "my-image.png"
        #cv2.imwrite(img_item, roi_frame)

        colour = (255, 0, 0) #BGR
        stroke = 2
        fx = x + w #f for final
        fy = y + h
        
        cv2.rectangle(frame, (x,y),(fx,fy), colour, stroke) #defines a rectangle with x,y being the top left and fx,fy being the bottom right
                 
    cv2.imshow('frame',frame)

    if cv2.waitKey(20) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
