# encoding=utf8
import numpy as np
import cv2

filename = "../images/church01.jpg"

image = cv2.imread(filename, 0)
image_show = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

corners = cv2.goodFeaturesToTrack(image, 500, 0.01, 10)
print corners.shape, type(corners)
radius = 3
color = (0, 255, 255)
thickness = 1
for pt in corners:
    print pt, pt[0]
    cv2.circle(image_show, (pt[0][0], pt[0][1]), radius, color, thickness)

cv2.imshow('src gray', image)
cv2.imshow('harris Corners', image_show)
cv2.waitKey(15000)
cv2.destroyAllWindows()