from cv2 import cv2

#--image-paths--
path1='Resources/Ekh_r2BVkAIktLX.jpeg'
path2 = 'Resources/72131675.webp'
path3 = 'Resources/EmYVa7cU0AABoaz.jpeg'
paths = [path1,path2,path3]
count=0
#
#####
nplatecascade = cv2.CascadeClassifier('Resources/haarcascade_russian_plate_number.xml')
#####
for path in paths:
    img = cv2.imread(path)
    img = cv2.resize(img , (600,600))

    #convert the image to gray for detection
    imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    nplates = nplatecascade.detectMultiScale(imgGray,1.1,4)

    if (len(nplates) == 0):
        print('not found')
        cv2.putText(img,'NO Name Plate Found',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)
    else:
        for (x,y,w,h) in nplates:
            area = w*h
            if area > 1000:
                cv2.putText(img,'Number Plate',(x,y-25),cv2.FONT_ITALIC,1,(0,255,0),4)
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
                imgROI=img[y:y+h,x:x+w]
                cv2.imshow("Number plate" , imgROI)

    cv2.imshow('Image', img)

    if cv2.waitKey()==ord('s'):
        cv2.imwrite('Resources/Scanned/Number_plate_'+str(count)+'.jpeg',imgROI)
        cv2.rectangle(img,(0,250),(600,350),(0,255,0),cv2.FILLED)
        cv2.putText(img,'Image Scanned',(250,275),cv2.FONT_HERSHEY_COMPLEX,1,(0,100,0),0)
        cv2.imshow("Result" , img)
        cv2.waitKey(500)
        count += 1
    else :
        continue
cv2.destroyAllWindows()