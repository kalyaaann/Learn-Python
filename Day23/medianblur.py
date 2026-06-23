import cv2 
orignal_image = cv2.imread("pokhara.jpg")
image = cv2.resize(orignal_image, None, fx=0.5, fy=0.5)
medblur_img= cv2.medianBlur(image,5)

cv2.imshow("Orignal Image",image)
cv2.imshow("Median Blurred Image",medblur_img)
cv2.imwrite("medblurpkr.jpg",medblur_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
