import cv2.data
import cv2 as cv

webcam = cv.VideoCapture(0)

webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640 / 10)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480 / 10)

face_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml")

if not webcam.isOpened():
    print("Não foi possível abrir a camera")
    exit()

while True:
    window, frame = webcam.read()

    if not window:
        print("Não foi possível mostrar o frame! (Saindo...)")
        break

    imagem_normalizada = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        imagem_normalizada, 1.3, 5)

    print("Não Reconhecido")

    for (x1, y1, x2, y2) in faces:
        cv.rectangle(
            frame, (x1, y1), (x1 + y2, y1 + x2), (255, 150, 0), 2)

        if x1 and y1 and x2 and y2:
            print("Reconhecido")

    cv.imshow('Reconhecimento Facial com Python e OpenCV', frame)

    if cv.waitKey(1) == ord("q"):
        print("Você saiu!")
        break


webcam.release()
cv.destroyAllWindows()
