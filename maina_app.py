import cv2
import numpy as np

myColors = [[0, 100, 151 ,179, 247 ,255],
            [102 ,77, 118, 131, 255, 255],
            ]

def findColor(img,myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10, myColors[],cv2.FILLED)
        #cv2.imshow("img",mask)            

def getContours(img):
    contours,heirarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgResult,cnt,-1, (255,0,0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri,True)
            x,y,w,h = cv2.boundingRect(approx)    
    return x+w//2,y    

frame_height = 640
frame_width = 480
cap = cv2.VideoCapture(0)
cap.set(3,frame_width)
cap.set(4,frame_height)
cap.set(10,150)

while True:
    success , img = cap.read()
    imgResult = img.copy() 
    findColor(img,myColors)
    cv2.imshow("Webcam Video", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break