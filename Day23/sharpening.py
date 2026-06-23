import cv2 
import numpy as np 
image = cv2.imread("lowquality.jpg")
sharpen_kernel= np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
    ])
sharpen_img= cv2.filter2D(image,-1,sharpen_kernel)

cv2.imshow("Orignal Image",image)
cv2.imshow("Sharpened Image",sharpen_img)
cv2.imwrite("sharp_lowquality.jpg",sharpen_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
