import cv2 as cv

# Recognizer
ReconhecedorLBPH = cv.face.LBPHFaceRecognizer_create

# Classifier
ClassificadorCascata = cv.CascadeClassifier

# encapsulated putText()
def putText(img, texto, posicao):
    return cv.putText(img, texto, posicao, cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)