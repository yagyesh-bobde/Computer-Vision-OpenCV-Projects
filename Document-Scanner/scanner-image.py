from cv2 import cv2
import numpy as np

def pre_process_image(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgGray, 250, 250)
    kernel=np.ones((5,5))
    # imgDialte= cv2.dilate(imgCanny,kernel,iterations=2)
    # imgResult= cv2.erode(imgDialte,kernel,iterations=1)

    return imgCanny

def get_contours(img) :
    biggest = np.array([])
    maxArea = 0
    countour,_ =cv2.findContours(img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in countour:
        #cv2.drawContours(imgCnt, cnt, -1, (255, 0, 0), 4)
        area = cv2.contourArea(cnt)
        if area>5000:
            peri=cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            if area>maxArea and len(approx) == 4 :
                biggest = approx
                maxArea = area
        else:
            pass
    cv2.drawContours(imgCnt, biggest, -1, (255, 0, 0), 20)
    return biggest

def get_new_points(points):
    points = points.reshape(4,2)
    new_points = np.zeros(points.shape)
    sum = points.sum(1)
    new_points[0]= points[np.argmin(sum)]
    new_points[3] = points[np.argmax(sum)]
    diff = np.diff(points,axis=1)
    new_points[1] = points[np.argmin(diff)]
    new_points[2] = points[np.argmax(diff)]
    return new_points

def get_warp(img,biggest) :
    newPoints= get_new_points(biggest)
    pt1 = np.float32(newPoints)
    pt2 = np.float32([[0,0],[widthimg,0],[0,heightimg],[widthimg,heightimg]])
    matrix = cv2.getPerspectiveTransform(pt1,pt2)
    imgOutput = cv2.warpPerspective(img,matrix,(widthimg,heightimg))
    return imgOutput



#######
widthimg = 580
heightimg=480
#######
img = cv2.imread('Resources/image-1.jpeg')
img = cv2.resize(img,(widthimg,heightimg))
imgCnt=img.copy()
imgThresh = pre_process_image(img)

biggest = get_contours(imgThresh)
if len(biggest)==0:
    imgResult = img
else:
    imgResult = get_warp(img,biggest)

cv2.imshow('Image',img)
cv2.imshow('Canny', imgThresh)
cv2.imshow('Result',imgCnt)
cv2.imshow('Document Scanned',imgResult)
#cv2.imshow('Contour',imgContour)
cv2.waitKey(0)
cv2.destroyAllWindows()