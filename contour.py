import cv2

cap2 = cv2.imread('five.jpg', 0)

r, thresh1 = cv2. threshold(cap2, 127, 255, 0)
contour1, hierachy1 = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cnt1 = contour1[0]
cv2.drawContours(cap2, contour1, -1, (0, 255, 255), 1)
cv2.imshow('contour-1', cap2)
print(str(len(contour1)))

cv2.waitKey(0)
cv2.destroyAllWindows()