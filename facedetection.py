import cv2
hand_cascade = cv2.CascadeClassifier('harrcascade/Skk.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    A = hand_cascade.detectMultiScale(img, 1.1, 5)

    for (hx, hy, hw, hh) in A:
        cv2.rectangle(img, (hx, hy), (hx + hw, hy + hh), (125, 125, 0), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()