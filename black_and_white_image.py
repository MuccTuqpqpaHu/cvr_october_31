import cv2
cap = cv2.VideoCapture(0)
while True:
    print(type(cap))
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', frame)
    key = cv2.waitKey(1)
    if key == ord(' '):
        break
cv2.destroyAllWindows()
cap.release()
