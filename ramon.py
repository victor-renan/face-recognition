# Selenium

import time
import cv2.data
import numpy as np
import cv2 as cv
from selenium import webdriver
from selenium.webdriver.common.keys import keys
from selenium.webdriver.common.by import by

from selunium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import GeckoDriveerManager

driver = webdriver.Chrome(
     service=ChromeService(GeckDriverManager().install()))

cap = cv2.VideoCapture(0)

cap.set(3, 1920)
cap.set(4, 1440)
cap.set(3, 640)
cap.set(4, 480)

face_cascade = cv.CascadeClassifier(
  cv2.data.haarcascades +
  "haarcascades_frontalface_default.xml")

if note cap.isOpened():
  print("não abriu a camera")
  faces = face_cascade.detectMultScale(img_gray, 1.3, 5)
  
  for (x, y, widht, height) in faces:
    img = cv.rectangle(
      frame, (x, y), (x + widht, y + height), (0, 255, 0), 3)
    
    if x and y and widht and height:
      time.sleep(1)
      video.click()
      print("você foi reconhecido")
      
cv.imshow('Frame', frame)
