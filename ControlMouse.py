import cv2
import time
import numpy as np
import module as htm
import autopy

wCam, hCam = 640, 480
pTime = 0
smoothenImg = 7
plocX, plocY = 0, 0
clocX, clocY = 0, 0
detector = htm.handDetector(maxHands=1)
frameR = 100  # frame Reduction
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
cap.set(10, 100)
wScr, hScr = autopy.screen.size()

while True:
    # 1. Find hand landmarks
    success, imgO = cap.read()
    img = cv2.flip(imgO, 1)
    img = detector.findHands(img)
    lmList = detector.findPosition(img)

    # 2. Get tip of index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # 3. Check which fingers are up
        fingers = detector.fingersUp()
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

        # 4. Only index Fingers: moving mode
        if fingers[1] == 1 and fingers[2] == 0:
            # 5. Convert Coordinates
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            # 6. Smoothen Value
            clocX = plocX + (x3 - plocX) / smoothenImg
            clocY = plocY + (y3 - plocY) / smoothenImg

            # 7. Move Mouse
            autopy.mouse.move(clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 0), -1)
            plocX, plocY = clocX, clocY

        # 8. Both index and middle fingers are up: Clicking mode
        if fingers[1] == 1 and fingers[2] == 1:
            # 9. Find distance between fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)
            # print(length)
            # 10. Click mouse if distance short
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), -1)
                autopy.mouse.click()

    # 11. Frame rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_ITALIC, 2, (255, 255, 255), 2)
    # 12. Display
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
