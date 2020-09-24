import argparse
import cv2

# construct the parser

# ap = argparse.ArgumentParser()
# ap.add_argument("-i","--image", required=True,help = "Path to image")
# args = vars(ap.parse_args())
# print(args["image"])

image_path = "data/tetris_blocks.png"
image = cv2.imread(image_path)

#conver to grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# cv2.imshow("image",gray)
# cv2.waitKey(0)


# Edge detection

edged = cv2.Canny(gray,30,150)


# Thresholding
thresh = cv2.threshold(gray,225,255,cv2.THRESH_BINARY_INV)[1]

# find contours
cnts,_ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
output = image.copy()

for c in cnts:
    cv2.drawContours(output,[c],-1,(240,0,159),3)

cv2.imshow("edge",output)
cv2.waitKey(0)