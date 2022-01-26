from cv2 import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

vid = cv2.VideoCapture(1)
detector = FaceMeshDetector(maxFaces=1 )

while 1:
    suc, frame = vid.read()
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
        # print(w)
        ##finding the focal point

        # d = 43
        # f= (w*d) /W
        # print(f)

        f = 1070
        d = (W*f)/w
        cvzone.putTextRect(img,f'Distance {int(d)} cm',(face[10][1] , face[10][1]))



    cv2.imshow("CAMERA", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()