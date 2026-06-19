import cv2

image = cv2.imread("nepalflag.jpg")

if image is None:
    print("Error in showing up the image")
else:
    print("Image loaded Successfully")

#image show
import cv2
image=cv2.imread("nepalflag.jpg")
cv2.imshow("Flag of Nepal",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# #save image
cv2.imwrite("2ndimgflag.jpg",image)


#image dimensions. 
import cv2
image=cv2.imread("nepalflag.jpg")

if image is not None:
    h,w,c = image.shape
    print(f"Image Loaded : \n Height :{h}\n Width : {w}\n Channels: {c}")
else:
    print("Error: Image couldnot load successfully")

#grayscale conversion 
import cv2
image=cv2.imread("nepalflag.jpg")

if image is not None:
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Scale Image",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Error: Image couldnot load successfully")

cv2.imwrite("grayflag.jpg",gray)