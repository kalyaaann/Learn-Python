import cv2

image = cv2.imread("triangle.png")
gray_image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh =cv2.threshold(gray_image,240,255,cv2.THRESH_BINARY)

#find contours 
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#draw contours
cv2.drawContours(image, contours,-1,(0,255,0),3)

cv2.imshow("Contours image",image)
cv2.imwrite("contourtriangle.jpg",image)

cv2.waitKey()
cv2.destroyAllWindows()