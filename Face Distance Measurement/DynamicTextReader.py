from cv2 import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import numpy as np



cam = cv2.VideoCapture(1)
#########
cam.set(3,480)
cam.set(4,640)
cam.set(10,100)
#########

detector = FaceMeshDetector(maxFaces=1 )

texts = ['This is DeepDive', 'Here you\' going', 'to learn Everything about','Machine Learning','Like Share'+'&'+'Subscribe','for more content!']
sen = 10
while 1:
    suc, frame = cam.read()
    text_img = np.zeros_like(frame)
    if (not suc) :
        print("No image")
        break
    img, faces = detector.findFaceMesh(frame,draw=False)
    if faces :
        face = faces[0]
        left = face[145]
        right = face[374]
        # cv2.circle(img,left,5,(0,200,0),cv2.FILLED)
        # cv2.circle(img, right, 5, (00,200, 0), cv2.FILLED)
        W = 6.3  # the avg distance (in cm) between the eyes of men and women i.e our reference for this project
        w,_,_= detector.findDistance(right, left, img )
        f = 1070

        ##calculate the distance
        d = (W*f)/w
        #show the distance on the feed
        cvzone.putTextRect(img,f'Distance {int(d)} cm',(face[10][1]+100 , face[10][1]-30),2,1)

        for i,text in enumerate(texts) :
            height = 30 + int((int(d/sen)*sen)/4)
            scale = 0.3 + (int(d/sen)*10)/100
            cv2.putText(text_img,text,(50,50+(i * height)) ,
                            cv2.FONT_HERSHEY_TRIPLEX,scale,(255,255,255),2)

    ##stack the cam feed and text side by side and show
    stack_img = cvzone.stackImages([img,text_img] , 2 , 1)
    cv2.imshow("CAMERA", stack_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()