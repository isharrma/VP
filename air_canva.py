import cv2
import numpy as np

def empty(a):
    pass

kernel = np.ones((5,5),np.uint8)

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
    imgflip = cv2.flip(img, 1)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min","Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min","Trackbars")
    v_min = cv2.getTrackbarPos("Val Min","Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max","Trackbars")
    s_max = cv2.getTrackbarPos("Sat Min","Trackbars")
    v_max = cv2.getTrackbarPos("Val Min","Trackbars")
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    
    mask = cv2.inRange(imgHSV,lower,upper)
    mask = cv2.erode(mask,kernel,iterations=1)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN,kernel)
    mask = cv2.dilate(mask,kernel, iterations=1)

    getContours(imgCanny)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("Mask",mask)
    cv2.imshow("Image",imgflip)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 