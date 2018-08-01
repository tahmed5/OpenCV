import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0) #able to change number value to select different cameras


while True:
    start = time.time()
    ret, frame = cap.read() #read function returns the retval and image
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    cv2.imshow('frame',frame) #displays the image to screen
    cv2.imshow('grey', grey)
    end = time.time()
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

print('FPS', 1/(end-start))

cap.release()
cv2.destroyAllWindows()
