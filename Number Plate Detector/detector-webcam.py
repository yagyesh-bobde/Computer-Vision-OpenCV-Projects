from cv2 import cv2
########
url='http://192.168.1.50:8080/video'
cam = cv2.VideoCapture(url)
nplate = cv2.CascadeClassifier('Resources/haarcascade_russian_plate_number.xml')
########

### --screen recording instead of webcam
# from vidgear.gears import ScreenGear
#
# # define dimensions of screen w.r.t to given monitor to be captured
# options = {'top': 20, 'left': 0, 'width': 1000, 'height': 1000}
#
# # open video stream with defined parameters
# stream = ScreenGear(monitor=1, logging=True, **options).start()
##
count = 0
while 1:
    res,frame = cam.read()
    frame = cv2.resize(frame,(600,600))
    imgGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    nplates = nplate.detectMultiScale(imgGray,1.1,4)
    if len(nplates) >0 :
        for (x, y, w, h) in nplates:
            area = w * h
            if area > 1000:
                cv2.putText(frame, 'Number Plate', (x, y - 25), cv2.FONT_ITALIC, 1, (0, 255, 0), 4)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 1)
                imgROI = frame[y:y + h, x:x + w]
                cv2.imshow("Number plate", imgROI)
    elif len(nplates)==0 :
        cv2.putText(frame,'NO Name Plate Found',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF==ord('s'):
        cv2.imwrite('Resources/Scanned/Number_plate_webcam' + str(count) + '.jpeg', imgROI)
        cv2.rectangle(frame, (0, 250), (600, 350), (0, 255, 0), cv2.FILLED)
        cv2.putText(frame, 'Image Scanned', (250, 275), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 100, 0), 0)
        cv2.imshow("Result", frame)
        cv2.waitKey(500)
        count += 1
    elif cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
cam.release()