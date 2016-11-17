%matplotlib inline

import cv2
import matplotlib.pyplot as plt
import time
import math

def find_target(im):
    # cv2.threshold(im, 250, 255, cv2.THRESH_BINARY, im)
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    # cv2.drawContours(im,contours,0,(255,0,255),1)

    (x,y),radius = cv2.minEnclosingCircle(contours[0])
    center = (int(x),int(y))
    radius = int(radius)
    target_size = len(im[0])/80
    cv2.circle(im,center,target_size,(0,255,0),target_size/2)

    FOV = 60.0
    camera_width = len(im[0])
    slope = FOV/camera_width
    intercept = -FOV/2.0
    angle = (x*slope)+intercept
    return (angle)


for res in [1280, 640, 320, 160, 80]:
    start = time.clock()
    im = cv2.imread("./images/14_00_" + str(res) + ".png")
    angle = find_target(im)
    end = time.clock()
    print str(len(im[0])) + " x " + str(len(im)) + " px"
    print "Time: " + str(math.floor(1.0/(end-start))) + " FPS"
    print "Computed Angle: " + str(angle)
