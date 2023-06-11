import cv2 as cv
from PIL import Image
import numpy as np
import os

reconhecedor = cv.face.LBPHFaceRecognizer_create(
    radius=2, neighbors=3, grid_x=8, grid_y=8)

classificador = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml")


def classificar_imagens(pasta):
    imagens = [os.path.join(pasta, f) for f in os.listdir(pasta)]

    print(imagens)

    rostos_finais = []
    indexes = []
    labels = []

    for imagem in imagens:
        img = Image.open(imagem).convert("L")
        img = np.array(img, 'uint8')

        index = imagens.index(imagem)

        rostos = classificador.detectMultiScale(img, 1.3, 5)

        for (x, y, w, h) in rostos:
            rostos_finais.append(img[y:y+h, x:x+w])
            labels.append(imagem.split('/')[-1].split('.')[0])
            indexes.append(index)

    return rostos_finais, indexes, labels


rostos, indexes, labels = classificar_imagens('./fotos')

reconhecedor.train(rostos, np.array(indexes))
reconhecedor.write('./modelos/modelo.yml')

with open('./modelos/modelo.txt', 'w') as f:
    for label in labels:
        f.write(label)
        f.write('\n')

    f.close()


print(f"{len(np.unique(indexes))} rostos treinados, {indexes}")
