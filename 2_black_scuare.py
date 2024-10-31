import cv2
cap = cv2.VideoCapture(0)
sl = int(input())
while True:
    ret, frame = cap.read()
    print(frame.shape)
    heigh, width, _ = frame.shape
    frame[heigh - sl:, width - sl:] = [0,0,0]
    frame[:sl, width - sl:] = [0,0,0]
    frame[heigh - sl:, :sl] = [0,0,0]
    frame[:sl, :sl] = [0,0,0]
    frame[heigh//2 - sl//2:heigh//2 + sl//2, width//2 - sl//2:width//2 + sl//2] = [0,0,0]
    cv2.imshow("camera", frame)
    cv2.waitKey(1)