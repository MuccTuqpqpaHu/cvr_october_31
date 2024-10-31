import cv2
from pprint import pprint
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    print(ret)
    for i in frame:
        for el in i:
            print(el, end="")
        print()
    cv2.imshow("camera", frame)
    cv2.waitKey(1)
    break