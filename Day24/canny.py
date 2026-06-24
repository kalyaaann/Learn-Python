import cv2

orignal_image = cv2.imread("flower.jpg",cv2.IMREAD_GRAYSCALE)
image = cv2.resize(orignal_image, None, fx=0.5, fy=0.5)

edges= cv2.Canny(image,50,150)

cv2.imshow("Orignal Image",image)
cv2.imshow("Edges",edges)
cv2.imwrite("canny_img.jpg",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
