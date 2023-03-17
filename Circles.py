import numpy as np
import argparse
import cv2
path = r'C:\Users\Anthony\Desktop\IPPractice\images\sample1.png'
image = cv2.imread(path)
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# detect circles in the image

#circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
              param1=30,
              param2=15,
              minRadius=80,
              maxRadius=100)
print(circles)
#cv2.imshow("output", gray)
#cv2.imshow("output",output)
# ensure at least some circles were found
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    print("true")
    for(x,y,r) in circles:
        cv2.circle(output, (x,y),r, (0,255,0), 4)
    cv2.imshow("output",output)
    cv2.waitKey(0)
