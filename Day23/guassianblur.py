import cv2 
orignal_image = cv2.imread("nepal.webp")
image = cv2.resize(orignal_image, None, fx=0.5, fy=0.5)
blur_img= cv2.GaussianBlur(image,(7,7),3)

cv2.imshow("Orignal Image",image)
cv2.imshow("Blurred Image",blur_img)
cv2.imwrite("guassianblur_nepal.jpg",blur_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
