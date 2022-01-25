from cv2 import cv2
#import cvzone
#from cvzone.FaceMeshModule import FaceMeshDetector

vid = cv2.VideoCapture(0)
#detector = FaceMeshDetector(maxFaces=1 )

while 1:
    suc, frame = vid.read()
    if (not suc) :
        print("No image")
        break
    #img, faces = detector.findFaceMesh(frame)
    cv2.imshow("CAMERA", img)
    cv2.waitKey(1)
