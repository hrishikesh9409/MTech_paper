import cv2.cv as cv
import time

cv.NamedWindow("camera", 1)

capture = cv.CaptureFromCAM(0)
img = cv.QueryFrame(capture)
cv.ShowImage("camera", img)

cv.SaveImage('password.jpg', img)
ts = time.time()

with open("TIMESTAMP.DAT", "w") as text_file:
	text_file.write(str(ts))

#print ts


