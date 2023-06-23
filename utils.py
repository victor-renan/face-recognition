import cv2 as cv
import numpy as np
import os


# Recognizer
ReconhecedorLBPH = cv.face.LBPHFaceRecognizer_create

# Classifier
ClassificadorCascata = cv.CascadeClassifier

# encapsulated putText()
def escrever(imagem, texto, posicao):
    return cv.putText(imagem, texto, posicao, cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

def quadrado(imagem, x, y, w, h):
    return cv.rectangle(imagem, (x, y), (x+w, y+h), (255, 0, 0), 2)

# get image names from path
def obter_imagens_da_pasta(pasta):
    return [os.path.join(pasta, img) for img in os.listdir(pasta)]

# convert filename to string
def obter_nome_imagem(imagem):
    return imagem.split('/')[-1].split('\\')[-1].split('.')[0].capitalize()

# transform an image to array
def imagem_para_array(imagem):
    imagem_norm = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)
    imagem_norm = np.array(imagem_norm, 'uint8')
    return imagem_norm

# test an image with opencv
def teste_img(imagem):
    while True:
        cv.imshow("Teste", imagem)

        if cv.waitKey(1) == 27:
            break