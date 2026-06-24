import cv2

orignal_image = cv2.imread("flower.jpg",cv2.IMREAD_GRAYSCALE)
image = cv2.resize(orignal_image, None, fx=0.5, fy=0.5)

ret, thresh_img= cv2.threshold(image,120,255,cv2.THRESH_BINARY)

cv2.imshow("Orignal Image",image)
cv2.imshow("Threshold image",thresh_img)
cv2.imwrite("threshold_img.jpg",thresh_img)

cv2.waitKey(0)
cv2.destroyAllWindows()