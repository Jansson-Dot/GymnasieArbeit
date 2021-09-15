import cv2

img = cv2.VideoCapture(0)

cv2.imshow("Video", img)


cv2.waitKey(0)