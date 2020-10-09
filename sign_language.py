import cv2

hand_cascade = cv2.CascadeClassifier('harrcascade/palm.xml')
fist_cascade = cv2.CascadeClassifier('harrcascade/fist.xml')
C_cascade = cv2.CascadeClassifier('harrcascade/C4.xml')
E_cascade = cv2.CascadeClassifier('harrcascade/E5.xml')
D_cascade = cv2.CascadeClassifier('harrcascade/D5.xml')
F_cascade = cv2.CascadeClassifier('harrcascade/F2.xml')
G_cascade = cv2.CascadeClassifier('harrcascade/G5.xml')
H_cascade = cv2.CascadeClassifier('harrcascade/H.xml')
I_cascade = cv2.CascadeClassifier('harrcascade/I.xml')
K_cascade = cv2.CascadeClassifier('harrcascade/K4_24.xml')
L_cascade = cv2.CascadeClassifier('harrcascade/L.xml')

O_cascade = cv2.CascadeClassifier('harrcascade/O.xml')
P_cascade = cv2.CascadeClassifier('harrcascade/P.xml')
Q_cascade = cv2.CascadeClassifier('harrcascade/Q.xml')
R_cascade = cv2.CascadeClassifier('harrcascade/R.xml')

T_cascade = cv2.CascadeClassifier('harrcascade/T1.xml')
U_cascade = cv2.CascadeClassifier('harrcascade/U1.xml')
W_cascade = cv2.CascadeClassifier('harrcascade/W.xml')

Y_cascade = cv2.CascadeClassifier('harrcascade/Y2.xml')

nice_cascade = cv2.CascadeClassifier('harrcascade/nice.xml')
bad_cascade = cv2.CascadeClassifier('harrcascade/bad.xml')
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.rectangle(frame, (100, 100), (350, 350), (0, 255, 0), 3)
    crop = frame[100:350, 100:350]
    crop_img = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)

    #one = one_cascade.detectMultiScale(crop_img)
    A = fist_cascade.detectMultiScale(crop_img, 2, 5)
    B = hand_cascade.detectMultiScale(crop_img, 1.3, 5)
    C = C_cascade.detectMultiScale(crop_img, 1.3, 5)
    D = D_cascade.detectMultiScale(crop_img, 1.3, 5)
    E = E_cascade.detectMultiScale(crop_img)
    F = F_cascade.detectMultiScale(crop_img, 1.1, 5)
    G = G_cascade.detectMultiScale(crop_img, 3.5, 5)
    H = H_cascade.detectMultiScale(crop_img, 1.6, 5)
    I = I_cascade.detectMultiScale(crop_img)
    K = K_cascade.detectMultiScale(crop_img, 3, 4)
    L = L_cascade.detectMultiScale(crop_img, 1.3, 4)

    O = O_cascade.detectMultiScale(crop_img, 1.2, 5)
    P = P_cascade.detectMultiScale(crop_img, 1.3, 5)
    Q = Q_cascade.detectMultiScale(crop_img)
    R = R_cascade.detectMultiScale(crop_img, 1.3, 5)

    W = W_cascade.detectMultiScale(crop_img, 1.2, 5)

    Y = Y_cascade.detectMultiScale(crop_img, 1.3, 5)
    T = T_cascade.detectMultiScale(crop_img)
    U = U_cascade.detectMultiScale(crop_img)

    nice = nice_cascade.detectMultiScale(crop_img, 1.3, 5)
    bad = bad_cascade.detectMultiScale(crop_img, 1.3, 5)

    for (hx, hy, hw, hh) in A:
        cv2.putText(frame, 'A', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)
    for (hx, hy, hw, hh) in B:
        cv2.putText(frame, 'B', (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)
    for (hx, hy, hw, hh) in C:
        cv2.putText(frame, 'C', (60, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)
    for (hx, hy, hw, hh) in D:
        cv2.putText(frame, 'D', (80, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)
    for (hx, hy, hw, hh) in E:
        cv2.putText(frame, 'E', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)
    for (hx, hy, hw, hh) in F:
        cv2.putText(frame, 'F', (120, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)
    for (hx, hy, hw, hh) in G:
        cv2.putText(frame, 'G', (140, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)
    for (hx, hy, hw, hh) in H:
        cv2.putText(frame, 'H', (160, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)
    for (hx, hy, hw, hh) in I:
        cv2.putText(frame, 'I', (180, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)
    for (hx, hy, hw, hh) in K:
        cv2.putText(frame, 'K', (200, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)
    for (hx, hy, hw, hh) in L:
        cv2.putText(frame, 'L', (220, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)
    
    for (hx, hy, hw, hh) in O:
        cv2.putText(frame, 'O', (260, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)
    for (hx, hy, hw, hh) in P:
        cv2.putText(frame, 'P', (280, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)
    for (hx, hy, hw, hh) in Q:
        cv2.putText(frame, 'Q', (300, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)
    for (hx, hy, hw, hh) in R:
        cv2.putText(frame, 'R', (320, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)

    for (hx, hy, hw, hh) in W:
        cv2.putText(frame, 'W', (400, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)

    for (hx, hy, hw, hh) in Y:
        cv2.putText(frame, 'Y', (400, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)
    for (hx, hy, hw, hh) in T:
        cv2.putText(frame, 'T', (400, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)
    for (hx, hy, hw, hh) in U:
        cv2.putText(frame, 'U', (400, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)

    for (hx, hy, hw, hh) in nice:
        cv2.putText(frame, 'Nice', (100, 400), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)
    for (hx, hy, hw, hh) in bad:
        cv2.putText(frame, 'Bad', (100, 400), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('cropped', crop)
    cv2.imshow('Main', frame)

    if cv2.waitKey(3) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()