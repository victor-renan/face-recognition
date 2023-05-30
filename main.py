import time
import cv2.data
import numpy as np
import cv2 as cv

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

face_cascade = cv.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

if not cap.isOpened():
    print("Não foi possível abrir a camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Não foi possível mostrar o frame! (Saindo...)")
        break

    img_gray = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    faces = face_cascade.detectMultiScale(img_gray, 1.3, 5)

    for (x, y, width, height) in faces:
        img = cv.rectangle(
            frame, (x, y), (x + width, y + height), (0, 255, 0), 3)

        if x and y and width and height:
            time.sleep(1)
            video.click()
            print("Reconhecido")


    cv.imshow('Frame', frame)

    if cv.waitKey(1) == ord("q"):
        print("Saindo...")
        break


cap.release()
cv.destroyAllWindows()
