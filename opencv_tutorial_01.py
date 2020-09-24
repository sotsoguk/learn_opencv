# import imutils
import cv2

image = cv2.imread('data/img1.jpg')
(h,w,d) = image.shape

print(f'w = {w}, h = {h}, d = {d}')

# create ROI
roi = image[100:500,300:400]
# cv2.imshow("ROI",roi)

# resize image
# compute aspect ratio
ratio = float(h) / float(w)

resized = cv2.resize(image,(300,int(300*ratio)))

# rotate image
center = (w//2,h//2)
M = cv2.getRotationMatrix2D(center,-45,1.0)

rotated = cv2.warpAffine(image,M,(w,h))

#blur image
blurred = cv2.GaussianBlur(image,(11,11),0)


# put text

txted = image.copy()
cv2.putText(txted,"Me and my Inspector",(50,50),cv2.FONT_HERSHEY_PLAIN,4.0,(200,200,200),2)
# draw something
output = image.copy()
cv2.rectangle(output,(100,0),(400,100),(255,0,),2) # color is BGR
cv2.imshow("image",image)
cv2.imshow("resized",txted)
cv2.waitKey(0)