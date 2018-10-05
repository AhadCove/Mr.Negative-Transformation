import cv2
import numpy as np

img = cv2.imread('mrnegative.png', cv2.IMREAD_GRAYSCALE)

img = cv2.resize(img, (0, 0), fx=.35, fy=.35)

binary = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]

negative = cv2.bitwise_not(binary)

cv2.imshow("negative", negative)
cv2.waitKey(0)
cv2.destroyAllWindows()