import cv2
import numpy as np


def getContours(img):
    contours, heirarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)


frameHeight = 640
frameWidth = 480
cap = cv2.VideoCapture(0)
cap.set(3,frameHeight)
cap.set(4,frameWidth)
cap.set(10,150)

while True:
    success , img = cap.read()
    cv2.imshow("Img",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break