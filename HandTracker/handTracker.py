from cv2 import cv2
import time
from mediapipe import mediapipe as mp
import numpy as np


cam = cv2.VideoCapture(0)
########
cam.set(3,480)
cam.set(4,640)
cam.set(10,100)
########
ctime = 0
ptime = 0
#####
mpHands = mp.solutions.hands
Hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    res,frame = cam.read()
    frame = cv2.flip(frame,1)
    ### our hand tracker uses rgb image so we need to convert it first
    imgRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    Results = Hands.process(imgRGB)
    #print(Results.multi_hand_landmarks)
    h,w,c = frame.shape
    if Results.multi_hand_landmarks :
        for handLms in Results.multi_hand_landmarks :
            mpDraw.draw_landmarks(frame,handLms,mpHands.HAND_CONNECTIONS)
            for id,lm in enumerate(handLms.landmark) :
                cw,ch = int(lm.x*w) , int(lm.y*h)
                # if id ==0 :
                #     cv2.circle(frame,(cw,ch),100,(255,0,0),cv2.FILLED)
    else :
        pass

    #--FpS--
    ctime = time.time()
    fps = 1//(ctime-ptime)
    ptime = ctime
    cv2.putText(frame, str(int(fps)) , (frame.shape[1]-100 ,frame.shape[0]-25), cv2.FONT_HERSHEY_TRIPLEX, 2, (0,255,0), 2)
    #

    cv2.imshow('Hand Tracker',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()