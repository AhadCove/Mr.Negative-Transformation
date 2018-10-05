import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	(ret, frame) = cap.read()

	if ret:
		# Convert frame to gray
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Convert to black and white
		binary = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)[1]

		# Inverse the binary image from Black to white to White to black
		negative = cv2.bitwise_not(binary)

		cv2.imshow('negative', negative)
		k = cv2.waitKey(20)
		if k == 27:
			break

cap.release()
cv2.destroyAllWindows()