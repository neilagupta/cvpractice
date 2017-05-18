'''
Created on May 18, 2017

@author: neilagupta
'''

import cv2

cap = cv2.VideoCapture(0)

while(True):
    #Capture video frame by frame
    ret, frame = cap.read()
    
    #Operations in frame occur here (colorizes frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Display frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #End loop of capture when q is pressed
        break
    
#Release frame, capture and resources when everything is done
cap.release()
cv2.destroyAllWindows()
    