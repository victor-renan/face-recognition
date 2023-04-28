import time
import cv2.data
import numpy as np
import cv2 as cv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as BraveService
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.utils import ChromeType
# from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://www.youtube.com/watch?v=seoeYYzjGkw")

video = driver.find_element(By.ID, 'movie_player')
video.send_keys(Keys.SPACE)


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
