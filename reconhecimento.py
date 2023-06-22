import cv2 as cv
import constantes as cst

webcam = cv.VideoCapture(0)

webcam.set(cv.CAP_PROP_FRAME_WIDTH, 640 / 10)
webcam.set(cv.CAP_PROP_FRAME_WIDTH, 480 / 10)

if not webcam.isOpened():
    print("no foi possivel abrir a webcam")
    exit()

while True:
    janela, frame = webcam.read()

    if not janela:
        break
    
    if cv.waitKey(1) == cst.
