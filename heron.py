# Importar os pacotes que usaremos
import cv2 as cv

# Criar uma leitura na webcam
webcam = cv.VideoCapture(0)

# Configurar webcam
webcam.set(cv.CAP_PROP_FRAME_WIDTH, 640 / 10) # --> Configura a largura
webcam.set(cv.CAP_PROP_FRAME_HEIGHT, 480 / 10) # --> Configura a altura


# Cria um loop de leitura
while True:
    # Executa a leitura
    camera_aberta, tela = webcam.read()

    # Verifica se nao tem erros
    if not camera_aberta:
        print("ocorreu algum erro na webcam")
        break

    # Abre a janela com a tela
    cv.imshow("Reconhecimento Facial com Python e OpenCV", tela)

    # Cria um evento para fechar a janela
    if cv.waitKey(1) == 27:
        print("Fechando a webcam")
        break
    
    
# Aplica as regras da webcam
webcam.release()

# Quando o loop e encerrado destroi as janelas
cv.destroyAllWindows()
