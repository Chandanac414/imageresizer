import cv2
image = cv2.imread("chandana.jpg")
# cv2.imshow("title",image)
# cv2.waitKey(0)
scale=50
width=int(image.shape[1]*scale/100)
height=int(image.shape[0]*scale/100)
dsize=(width,height)
output=(cv2.resize(image,dsize))
cv2.imshow("resized image",output)
cv2.waitKey(0)
