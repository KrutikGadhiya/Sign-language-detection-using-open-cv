import cv2
import numpy as np

img1 = cv2.imread("one.jpg", cv2.IMREAD_GRAYSCALE)
#img2 = cv2.imread("five.jpg", cv2.IMREAD_GRAYSCALE)

img = cv2.VideoCapture(0)

# ORB Detector
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
cv2.imshow("Img1", img1)

while True:
    _, img3 = img.read()
    cv2.rectangle(img3, (100, 100), (350, 350), (0, 0, 255), 0)
    img_cropped = img3[100:350, 100:350]

    img2 = cv2.cvtColor(img_cropped, cv2.COLOR_BGR2GRAY)

    kp2, des2 = orb.detectAndCompute(img2, None)

    # Brute Force Matching
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key = lambda x:x.distance)


    matching_result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)

    cv2.imshow("Img2", img2)
    cv2.imshow("Matching result", matching_result)
    if cv2.waitKey(1) & 0xFF == 27:
        break


cv2.destroyAllWindows()