from matplotlib import pyplot as plt
import cv2
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

#Take input image and apply mask to get only capillaries(green stuff)
image = cv2.imread('images/sample1.png')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([31, 255, 0])
upper = np.array([179, 255, 255])
mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(image, image, mask=mask)
gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

cv2.imshow('image',image)
src = cv2.imread('images/sample1.png', cv2.IMREAD_UNCHANGED)
print(src.shape)


#clean up mask and create contours, counters are groupings of target capillaries
_ , mask = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)
cv2.imshow('mask2',mask) #clean mask that has isolated capillaries

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours_img_before_filtering = mask.copy()
contours_img_before_filtering = cv2.cvtColor(contours_img_before_filtering, cv2.COLOR_GRAY2BGR)
r2 = cv2.drawContours(contours_img_before_filtering, contours, -1, (0, 0, 255), 2) #need this so contours are actually drawn


#filter contours to find capillaries that are small 
count = 0
filtered_contours = []
for idx, contour in enumerate(contours):
    area = int(cv2.contourArea(contour))
    #count+=1
    # Attempt to filter out large capillaries is higher than 3000:
    if area < 10:
        filtered_contours.append(contour)
        count+=1


contours_img_after_filtering = mask.copy()
contours_img_after_filtering = cv2.cvtColor(contours_img_after_filtering, cv2.COLOR_GRAY2BGR)
r3 = cv2.drawContours(contours_img_after_filtering, tuple(filtered_contours), -1, (0, 255, 0), 2) #need this so filtered contours are actually drawn
cv2.imshow('contours.png', cv2.hconcat([image,contours_img_before_filtering, contours_img_after_filtering]))
print(len(contours_img_before_filtering))
print(count)

cv2.waitKey()
