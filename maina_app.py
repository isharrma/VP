import cv2
import numpy as np

myColors = [[0 ,82 ,165 ,179, 147 ,204],
            [0 ,179, 132, 212, 174, 231],
            ]

def findColor(img,myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array(myColors[0][0:3])
    upper = np.array(myColors[0][3:6])
    mask = cv2.inRange(imgHSV,lower,upper)
    cv2.imshow("img",mask)            

frame_height = 640
frame_width = 480
cap = cv2.VideoCapture(0)
cap.set(3,frame_width)
cap.set(4,frame_height)
cap.set(10,150)

while True:
    success , img = cap.read()
    findColor(img,myColors)
    cv2.imshow("Webcam Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break