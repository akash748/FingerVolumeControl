import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture(0)
current_time = 0
previous_time = 0

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
while True :
    success,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for i in results.multi_hand_landmarks:
            for id,lm in enumerate(i.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                #print(id,cx,cy)
            mpDraw.draw_landmarks(img,i,mpHands.HAND_CONNECTIONS)

    current_time = time.time()
    fps = 1/(current_time-previous_time)
    previous_time = current_time

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,255),4)


    cv2.imshow("Image",img)
    cv2.waitKey(1)

