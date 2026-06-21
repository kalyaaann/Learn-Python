    import cv2

    image= cv2.imread("pythonimg.png")

    if image is None:
        print("Error! Image not found")
    else:
        print("Image Loaded Successfully")
        pt1=(50,100)
        pt2=(300,100)
        color=(0,255,0)
        thickness=2
        line_img= cv2.line(image,pt1, pt2,color,thickness)

        cv2.imshow("Line draw",line_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    #rectangle draw


    ptr1=(50,100)
    ptr2=(300,200)
    color=(0,0,255)
    thickness=3
    rectangle_draw= cv2.rectangle(image,ptr1,ptr2,color,thickness)

    cv2.imshow("Rectangle draw",rectangle_draw)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    #circle draw


    circle_draw= cv2.circle(image,(150,150),50,(255,0,0),2)

    cv2.imshow("Circle draw",circle_draw)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #Adding texts to image

    add_text= cv2.putText(image,"Python Logo",(100,200),cv2.FONT_HERSHEY_DUPLEX,1.5,(0,0,255),3)

    cv2.imshow("Adding Text in image",add_text)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
