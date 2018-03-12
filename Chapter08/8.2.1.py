# encoding=utf8
import numpy as np
import cv2

filename = "../images/church01.jpg"

img = cv2.imread(filename, 0)
cornerStrength = cv2.cornerHarris(img, 3, 3, 0.01)

threshold = 0.0001
_, harrisCorners = cv2.threshold(cornerStrength, threshold, 255, cv2.THRESH_BINARY)

cv2.imshow('src gray', img)
cv2.imshow('harris Corners', harrisCorners)
cv2.waitKey(5000)
cv2.destroyAllWindows()