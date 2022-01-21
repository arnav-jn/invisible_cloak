import cv2
import numpy as np

cap = cv2.VideoCapture(0)
background = cv2.imread('./image.jpeg')

while cap.isOpened():
    ret, current_frame=cap.read()
    if ret:
        hsv_frame=cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)

        l_red=np.array([0,120,70])
        u_red=np.array([10,255,255])
        mask1 = cv2.inRange(hsv_frame, l_red, u_red)

        l_red = np.array([170, 120, 70])
        u_red = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv_frame, l_red, u_red)

        red_mask=mask1+mask2

        cv2.imshow("red mask", red_mask)
        if cv2.waitKey(5) == ord('s'):
            break
cap.release()
cv2.destroyAllWindows()
