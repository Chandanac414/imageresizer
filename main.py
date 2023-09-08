import cv2
image = cv2.imread("chandana.jpg")
# cv2.imshow("title",image)
# cv2.waitKey(0)
scale=50
width=int(input("Enter the desired width to resize"))
height=int(input("Enter the desired height to resize"))
dsize=(width,height)
output=(cv2.resize (image,dsize))
cv2.imshow("resized image",output)
cv2.waitKey(0)
