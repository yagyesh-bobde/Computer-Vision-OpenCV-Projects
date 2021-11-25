from cv2 import cv2
import time
from mediapipe import mediapipe as mp
import numpy as np

class handDetector() :
    def __init__(self,mode=False,maxHands=2,detectionCon=0.5,trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self,img,draw=True):
        '''
        This function tracks the hand and marks the landmark points on the hand
        and if True the it shows the line connecting the landmarks.
        :param img:  np.array,the image where we need to detect the hand
        :param draw: bool, wheter or not to draw the connections
        :return: the image with hand landmarks marked
        '''
        ### our hand tracker uses rgb image so we need to convert it first
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.Results = self.hands.process(imgRGB)
        #print(Results.multi_hand_landmarks)
        if self.Results.multi_hand_landmarks :
            for handLms in self.Results.multi_hand_landmarks :
                if draw:
                    self.mpDraw.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS)


        return img

    def findPosition(self,img,ids,handNO=0, draw=True ):
        '''
        it returns you the list of coordinates for the indexes you provide. It works on single hand
        or the right hand when both the hands are detected
        '''
        lmlist = []
        if self.Results.multi_hand_landmarks:
            myhand = self.Results.multi_hand_landmarks[handNO]
            for id, lm in enumerate(myhand.landmark):
                if id in ids:
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    # print(cx,cy)
                    lmlist.append([id, cx, cy])
                    cv2.circle(img, (cx, cy), 15, (50, 10, 10), cv2.FILLED)
        return lmlist

def main():
    cam = cv2.VideoCapture(0)
    ########
    cam.set(3, 480)
    cam.set(4, 640)
    cam.set(10, 100)
    ########
    ctime = 0
    ptime = 0
    #####
    detector = handDetector()
    while True:
        res, frame = cam.read()
        frame = cv2.flip(frame, 1)
        img = detector.findHands(frame)
        lmslist = detector.findPosition(img,ids=[0])
        print(lmslist)
        # --FpS--
        ctime = time.time()
        fps = 1 // (ctime - ptime)
        ptime = ctime
        cv2.putText(frame, str(int(fps)), (frame.shape[1] - 100, frame.shape[0] - 25), cv2.FONT_HERSHEY_TRIPLEX, 2,
                    (0, 255, 0), 2)

        cv2.imshow('Hand Tracker', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()