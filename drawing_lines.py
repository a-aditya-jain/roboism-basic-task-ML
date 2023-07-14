import math

import cv2 as cv
import numpy as np

img = np.ones((512,512,3))

flag = False
ix = -1
iy = -1
c = 1
pointx = []
pointy = []

def getm(pointx,pointy):
    m1 = (-(pointy[-3]-pointy[-2]))/(pointx[-3]-pointx[-2])
    print(m1)
    m2 = (-(pointy[-3]-pointy[-1]))/(pointx[-3]-pointx[-1])
    print(m2)
    print(m1 - m2)


    theta = math.atan(abs((m1-m2)/(1+m1*m2)))
    #print((m1-m2)/(1+m1*m2))
    #print(theta)
    if(pointx[-3]<pointx[-1]) :
        coo = str(math.trunc((theta*57.32)))

    if(pointx[-3]>pointx[-1]):
        coo = str(math.trunc(180-(theta * 57.32)))



    cv.putText(img, org = (pointx[-3],pointy[-3]), fontScale=0.7, color=(255,0,0), thickness=2, lineType=cv.LINE_AA, text=coo, fontFace=cv.FONT_ITALIC)

def draw(event, x, y, flags, params):
    global flag, ix, iy, c,pointx, pointy

    if event == 1:
        if c % 3 == 1:
            flag = True
            ix = x
            iy = y
            c += 1
            pointx.append(x)
            pointy.append(y)

        elif c % 3 == 2:
            flag = True
            cv.line(img, (ix, iy), (x, y), (0, 0, 255), 2)
            c += 1
            pointx.append(x)
            pointy.append(y)

        elif c % 3 == 0:
            flag = False
            cv.line(img, (ix, iy), (x, y), (0, 0, 255), 2)
            c += 1
            pointx.append(x)
            pointy.append(y)
            getm(pointx, pointy)
           # pointx=[0,0,0]
            #pointy=[0,0,0]


cv.namedWindow(winname="wind")
cv.setMouseCallback("wind", draw)

while True:
    cv.imshow("wind", img)
    if cv.waitKey(1) & 0xFF == ord('x'):
        break


