import cv2

video= cv2.VideoCapture(0)

while True :
    ret, frame = video.read()
    
    if not ret:
        print("Could not read frame")
        break
    cv2.imshow("Webcam Feed",frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        print("Quiting...")
        break
video.release()
cv2.destroyAllWindows()
