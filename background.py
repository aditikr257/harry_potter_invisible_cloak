import cv2
#this is my webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, back = cap.read() #here is an simple readin
    if ret:
        cv2.imshow("image", back)
        if cv2.waitKey(5) == ord('q'):
            #save the image
            cv2.imwrite('image.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()
