'''
Created on May 18, 2017

@author: neilagupta
'''

import cv2

cap = cv2.VideoCapture('Animation.mp4')
frame_counter = 0

while(cap.isOpened()):
    
    ret, frame = cap.read()
    
    frame_counter += 1
    #If the last frame of video then restart
    if frame_counter == cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
        frame_counter = 0
        cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, 0)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame',gray)
    
    #quit if key pressed is q
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
