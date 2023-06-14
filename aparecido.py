# Importar os pacotes que usaremos
import cv2 as cv
import numpy as np

# Criar uma leitura na webcam
webcam = cv.VideoCapture(0)

# Configurar webcam
webcam.set(cv.CAP_PROP_FRAME_WIDTH, 640 / 10) # --> Configura a largura
webcam.set(cv.CAP_PROP_FRAME_HEIGHT, 480 / 10) # --> Configura a altura



# Reconhecedor
reconhecedor = cv.face.LBPHFaceRecognizer_create(
    radius=2, neighbors=3, grid_x=8, grid_y=8)

reconhecedor.read('./modelos/modelo.yml')
labels = open('./modelos/modelo.txt', 'r').readlines()

print(labels)

classificador = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Cria um loop de leitura
while True:
    # Executa a leitura
    camera_aberta, tela = webcam.read()

    # Verifica se nao tem erros
    if not camera_aberta:
        print("ocorreu algum erro na webcam")
        break

    # Transformar nossa imagem em cinza
    imagem_cinza = cv.cvtColor(tela, cv.COLOR_BGR2GRAY)
    
    # Passar nosso vídeo na cor cinza para o código
    rostos = classificador.detectMultiScale(imagem_cinza, 1.3, 5)

    # BGR - azul, verde e vermelho
    for (x, y, w, h) in rostos:
        cv.rectangle(tela, (x, y), (x+w, y+h), (255, 0,0), 2)

        # Faz a comparação da pessoa da webcam com a do treinamento
        index, probabilidade = reconhecedor.predict(imagem_cinza[y:y+h, x:x+w])

        # Tranforma a probabilidade em porcetagem 
        porcentagem = str(" {0}%".format(round(100 - probabilidade)))

        if (probabilidade < 100): #BGR
            # Nome da pessoa
            cv.putText(tela, labels[index].split('\n')[0], (x+5, y-5), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255,0), 2)
            # Porcetagem
            cv.putText(tela, porcentagem, (x+5, y+h-5), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255,0), 2)

            if (labels[index] == labels[2]):
                cv.putText(tela, "Liberado", (x+5, y+h+10), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255,0), 2)



    # Abre a janela com a tela
    cv.imshow("Reconhecimento Facial com Python e OpenCV", tela)



    # Cria um evento para fechar a janela
    if cv.waitKey(1) == 27:
        print("Fechando a webcam")
        break
    
    
# Aplica as regras da webcam
webcam.release()

# Quando o loop eh encerrado destroi as janelas
cv.destroyAllWindows()