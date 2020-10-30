import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.rectangle(frame, (100, 100), (350, 350), (0, 0, 255), 0)
    img_croped = frame[100:350, 100:350]

    cv2.imshow('frame', img_croped)
    cv2.imshow('main', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        cv2.imwrite('N34.bmp', img_croped)
        break

cv2.destroyAllWindows()