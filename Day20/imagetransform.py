import cv2
img=cv2.imread("potatoalu.jpg")
if img is None:
    print("Error: Image couldnot be load")
else:
    print("Image Loaded Successfully")
   
    #resizing image 
    resized=cv2.resize(img,(250,250))
    #real image
    cv2.imshow("Real image",img)
    #resized image 
    cv2.imshow("Resized Image",resized)
    cv2.imwrite("resized_potatoalu.jpg",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#cropping and slicing 

import cv2

img= cv2.imread("potatoalu.jpg")

if img is not None:
    cropped= img[150:300, 100:200]

    cv2.imshow("Cropped image",cropped)
    cv2.imshow("Orignal image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Image rotation and flipping 

import cv2
img= cv2.imread("potatoalu.jpg")

if img is None:
    print("Couldnot load image")
else:
    h,w=img.shape[:2]  #stores the height and width 
    center=(w//2,h//2) #integer division
    M=cv2.getRotationMatrix2D(center,90,1.0)
    rotated=cv2.warpAffine(img,M,(w,h))

    cv2.imshow("Rotated image",rotated)
    cv2.imshow("Orignal image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#Flipping 

import cv2
img= cv2.imread("potatoalu.jpg")

if img is None:
    print("Couldnot load image")
else:
    flipped_horizotal=cv2.flip(img,1)
    flipped_vertical=cv2.flip(img,0)
    flipped_both=cv2.flip(img,-1)

    
    cv2.imshow("Orignal image",img)
    cv2.imshow("HORIZONTAL image",flipped_horizotal)
    cv2.imshow("VERTICAL image",flipped_vertical)
    cv2.imshow("FLIPPED BOTH image",flipped_both)


    cv2.waitKey(0)
    cv2.destroyAllWindows()


