import cv2 as cv


# Face Cascade
CASCATA_ROSTOS = cv.data.haarcascades + "haarcascade_frontalface_default.xml"

# Recognizer
ReconhecedorLBPH = cv.face.LBPHFaceRecognizer_create

# Classifier
ClassificadorCascata = cv.CascadeClassifier

# Tecla ESC
ESC = 27

# encapsulated putText()
def putText(img, texto, posicao):
    return cv.putText(img, texto, posicao, cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)