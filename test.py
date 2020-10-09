import cv2

hand_cascade = cv2.CascadeClassifier('harrcascade/palm.xml')
fist_cascade = cv2.CascadeClassifier('harrcascade/fist.xml')
C_cascade = cv2.CascadeClassifier('harrcascade/C3.xml')
one_cascade = cv2.CascadeClassifier('harrcascade/one-two.xml')


def check(original, duplicate):
    if original.shape == duplicate.shape:
        print("The images have same size and channels")
        difference = cv2.subtract(original, duplicate)
        b, g, r = cv2.split(difference)

        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            return True

    return False

def fun(image):
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(grey, (35, 35), 0)
    _, thresh1 = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contour, hierachy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    return contour


cap = cv2.VideoCapture(0)
A = cv2.imread('images/A.jpg', 1)
C = cv2.imread('images/C.jpg', 1)
#one = cv2.imread('one.jpg', 1)
two = cv2.imread('images/two.jpg', 1)
three = cv2.imread('images/three.jpg', 1)
four = cv2.imread('images/four.jpg', 1)
five = cv2.imread('images/five.jpg', 1)




cnt2 = fun(two)[0]
cv2.drawContours(two, fun(two), -1, (0, 255, 255), 1)
cv2.imshow('contour for two', two)
area_two = cv2.contourArea(fun(two)[0])

cnt3 = fun(three)[0]
cv2.drawContours(three, fun(three), -1, (0, 255, 255), 1)
cv2.imshow('contour for three', three)
area_three = cv2.contourArea(fun(three)[0])

cnt4 = fun(four)[0]
cv2.drawContours(four, fun(four), -1, (0, 255, 255), 1)
cv2.imshow('contour for four', four)
area_four = cv2.contourArea(fun(four)[0])

cnt5 = fun(five)[0]
cv2.drawContours(five, fun(five), -1, (0, 255, 255), 1)
cv2.imshow('contour for five', five)
area_five = cv2.contourArea(fun(five)[0])



area = -1
temp = 0
temp2 = 0
y = 0
while True:
    ret, frame = cap.read()

    cv2.rectangle(frame, (100, 100), (350, 350), (0, 0, 255), 2)
    img_cropped = frame[100:350, 100:350]

    grey1 = cv2.cvtColor(img_cropped, cv2.COLOR_BGR2GRAY)
    value = (35, 35)
    blurred = cv2.GaussianBlur(grey1, value, 0)
    _, thresh2 = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    hand = hand_cascade.detectMultiScale(frame, 1.3, 5)
    fist = fist_cascade.detectMultiScale(frame, 1.3, 5)
    C = C_cascade.detectMultiScale(frame)
    one = one_cascade.detectMultiScale(frame)

    for (hx, hy, hw, hh) in one:
        #cv2.rectangle(img_cropped, (hx, hy), (hx + hw, hy + hh), (125, 125, 0), 2)
        cv2.putText(img_cropped, '1', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)


    for (hx, hy, hw, hh) in C:
        #cv2.rectangle(img_cropped, (hx, hy), (hx + hw, hy + hh), (125, 125, 0), 2)
        cv2.putText(img_cropped, 'C', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)

    for (hx, hy, hw, hh) in hand:
        #cv2.rectangle(img_cropped, (hx, hy), (hx + hw, hy + hh), (125, 125, 0), 2)
        cv2.putText(img_cropped, 'B', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)

    for (hx, hy, hw, hh) in fist:
        #cv2.rectangle(img_cropped, (hx, hy), (hx + hw, hy + hh), (125, 125, 0), 2)
        cv2.putText(img_cropped, 'A', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)

    contour2, hierachy2 = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cnt2 = contour2[0]

    area_frame = cv2.contourArea(cnt2)

    cv2.drawContours(img_cropped, contour2, -1, (0, 255, 0), 1)

    x1, y1, w1, h1 = cv2.boundingRect(cnt2)
    cv2.rectangle(frame, (x1 + 100,y1 + 100),(x1 + w1 + 100, y1 + h1 + 100), (0, 255, 0), 2)
    cv2.imshow('Main', frame)

    #y = temp2
    #x = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
    #temp2 = x

    #temp = min(y, x)

    #if abs(area_frame - area_one) <= 2000 or check(one, frame):
        #print('1')
        #cv2.putText(img_cropped, '1', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)

    if abs(area_frame - area_two) <= 2000 or check(two, frame):
        print('2')
        cv2.putText(img_cropped, '2', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    elif abs(area_frame - area_three) <= 2000 or check(three, frame):
        print('3')
        cv2.putText(img_cropped, '3', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    elif abs(area_frame - area_four) <= 2000 or check(four, frame):
        print('4')
        cv2.putText(img_cropped, '4', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    elif abs(area_frame - area_five) <= 2000 or check(five, frame):
        print('5')
        cv2.putText(img_cropped, '5', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    #else:
        #print('Noting found')
        #cv2.putText(img_cropped, 'No Match', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)

    cv2.imshow('contour-2', img_cropped)
    #print(area_frame - area_one)

    if cv2.waitKey(1) & 0xFF == 27:
        break

print(temp)
cap.release()
cv2.destroyAllWindows()