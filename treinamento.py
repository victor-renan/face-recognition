import cv2 as cv
from PIL import Image
import numpy as np
import os

reconhecedor = cv.face.LBPHFaceRecognizer_create()

classificador = cv.CascadeClassifier(
  cv.data.haarcascades + "haarcascade_frontalface_default.xml")

def classificarImagens(pasta):
  imagens = [os.path.join(pasta, f) for f in os.listdir(pasta)]

  print(imagens)

  rostos_finais = []
  indexes = []

  for imagem in imagens:
      img = Image.open(imagem).convert("L")
      img = np.array(img, 'uint8')

      index = imagens.index(imagem)      
      rostos = classificador.detectMultiScale(img)

      for (x, y, w, h) in rostos:
          rostos_finais.append(img[y:y+h, x:x+w])
          indexes.append(index)

  return rostos_finais, indexes

rostos, indexes = classificarImagens('./fotos')

reconhecedor.train(rostos, np.array(indexes))
reconhecedor.write('model.yml')

print(f"{len(np.unique(indexes))} rostos treinados, {indexes}")
