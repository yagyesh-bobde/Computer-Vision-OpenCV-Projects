import math
from cv2 import cv2
import time
import pycaw   #https://github.com/AndreMiras/pycaw
import handTrackingModule as htm
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#####################
cam = cv2.VideoCapture(0)
########
cam.set(3, 480)
cam.set(4, 640)
cam.set(10, 100)
########
ctime = 0
ptime = 0
#####
detector = htm.handDetector(trackCon=0.75,detectionCon=0.75)
#####Audio#####
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMute()
volume.GetMasterVolumeLevel()
print(volume.GetVolumeRange())
volume.SetMasterVolumeLevel(-20.0, None)
def finger_vol(img,lmslist):
        x1,y1 = lmslist[0][1],lmslist[0][2]
        x2,y2 = lmslist[1][1],lmslist[1][2]
        cv2.circle(img, (x1,y1), 15, (100, 100, 100), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (100, 100, 100), cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),3)
        line_len = math.hypot(x2-x1,y2-y1)

        if line_len<40 :
            cv2.circle(img,((x1+x2)//2,(y1+y2)//2),15,(0,200,100),cv2.FILLED)

while True:
    res, frame = cam.read()
    frame = cv2.flip(frame, 1)
    img = detector.findHands(frame)
    lmslist = detector.findPosition(img,ids=[4,8])
    if len(lmslist) != 0:
        finger_vol(img,lmslist)
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