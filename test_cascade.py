import cv2
cascade = cv2.CascadeClassifier('harrcascade/fist.xml')

img = cv2.imread('images/B747.jpg')

B = cascade.detectMultiScale(img, 5, 5)

for (hx, hy, hw, hh) in B:
    cv2.rectangle(img, (hx, hy), (hx + hw, hy + hh), (125, 0, 0), 2)

cv2.imshow('Cascaded image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()