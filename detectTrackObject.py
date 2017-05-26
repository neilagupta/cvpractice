'''
Created on May 18, 2017

@author: neilagupta
'''
# import the needed packages
from collections import deque
import numpy as np
import argparse
import imutils
import cv2

# handle command line arguments and parse the arguments
ap = argparse.ArgumentParser()

#Argument for --video
ap.add_argument("-v", "--video",
    help="path to the (optional) video file")

#Argument for --buffer
ap.add_argument("-b", "--buffer", type=int, default=32,
    help="max buffer size")

#Parses all args
args = vars(ap.parse_args())

#Initializes all necessities of the points trail of the object
pts = deque(maxlen=args["buffer"])
counter = 0
(dx, dy) = (0, 0)
direction = ""

if not args.get("video", False):
    cap = cv2.VideoCapture(0)

while True:
    
    
    #If presses q at starting almost immediately
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break