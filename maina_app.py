import cv2
import numpy as np

myColors = [[0 ,87, 179, 179, 175, 255],
            [86 ,96, 70, 131, 142, 192],
            ]

def findColor(img,myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
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