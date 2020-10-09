import cv2

cap = cv2.VideoCapture(0)
cap2 = cv2.imread('five.jpg', 0)

r, thresh1 = cv2. threshold(cap2, 127, 255, 0)
contour1, hierachy1 = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cnt1 = contour1[0]
cv2.drawContours(cap2, contour1, -1, (0, 255, 255), 1)
cv2.imshow('contour-1', cap2)
temp = 0
temp2 = 0
y = 0
while True:
    ret, frame = cap.read()

    cv2.rectangle(frame, (100, 100), (350, 350), (0, 0, 255), 0)
    img_croped = frame[100:350, 100:350]

    gray = cv2.cvtColor(img_croped, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    edge = cv2.Canny(blurred, 100, 100)
    r2, thresh2 = cv2.threshold(gray, 127, 255, 0)
    contour2, hierachy2 = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cnt2 = contour2[0]

    cv2.drawContours(img_croped, contour2, -1, (0, 255, 0), 1)
    cv2.imshow('contour-2', img_croped)
    #cv2.imshow('cropped', edge)
    cv2.imshow('Main', frame)

    y = temp2
    x = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
    temp2 = x

    temp = min(y, x)
    #print(x)
    #cv2.imshow('Cropped Main', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

print(temp)
cap.release()
cv2.destroyAllWindows()