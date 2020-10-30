import cv2
message = input("Enter the message")
file = open("images/bg.txt", 'r')
A = cv2.imread("images/A.jpg")
B = cv2.imread("images/B.jpg")
C = cv2.imread("images/C.jpg")
D = cv2.imread("images/D.jpg")
E = cv2.imread("images/E.jpg")
type(file)
for name in message:
    for f in file:
        fname = f.split('.')
        if name.upper() == fname[0]:
            image = "images/" + fname[0] + ".txt"
            print(image)
            img = cv2.imread(image)
            cv2.imshow("image", img)
