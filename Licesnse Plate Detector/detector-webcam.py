from cv2 import cv2
########
url='http://192.168.1.50:8080/video'
cam = cv2.VideoCapture(url)
nplate = cv2.CascadeClassifier('Resources/haarcascade_russian_plate_number.xml')
########
while 1:
    res,frame = cam.read()
    frame = cv2.resize(frame,(600,600))
    imgGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    nplates = nplate.detectMultiScale(imgGray,1.1,4)
    if len(nplates) >0 :
        for (x,y,w,h) in nplates:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
    else:
        pass
    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
cam.release()