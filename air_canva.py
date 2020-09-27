import cv2
import numpy as np

def empty(a):
    pass

frameHeight = 640
frameWidth = 480
cap = cv2.VideoCapture(0)
cap.set(3,frameHeight)
cap.set(4,frameWidth)
cap.set(10,150)

cv2.namedWindow("Trackbars")
cv2.createTrackbar("Hue Min","Trackbars",0,179,empty)
cv2.createTrackbar("Hue Max","Trackbars",179,179,empty)
cv2.createTrackbar("Sat Min","Trackbars",0,255,empty)
cv2.createTrackbar("Sat MAx","Trackbars",255,255,empty)
cv2.createTrackbar("Val Min","Trackbars",0,255,empty)
cv2.createTrackbar("Val Max","Trackbars",255,255,empty)

def bead(img,x,y ,radius):
    cv2.circle(img , (int(x),int(y)),int(radius),(0,255,0),2)

def getContours(img):
    contours,heirarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 0 :
            cv2.drawContours(img,cnt,-1,(255,0,0,2))
        

while True:
    success ,img = cap.read()
    imgCanny = cv2.Canny(img,200,200)
    #imgflip = cv2.flip(img, 1)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    getContours(imgCanny)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("Canny",imgCanny)
    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 