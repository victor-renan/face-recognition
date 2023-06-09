# IX Maratona de TI: Reconhecimento Facial com Python e OpenCV

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8.svg?style=for-the-badge&logo=OpenCV&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A.svg?style=for-the-badge&logo=Selenium&logoColor=white)

![Python e OpenCV](https://i.imgur.com/8yxaomz.png)

Seja bem vindo a oficina Reconhecimento Facial com Python e OpenCV! Abaixo estão algumas instruções que serão importantíssimas no decorrer do seu projeto. Preste bastante atenção nos comandos dos instrutores para que você não se perda nem fique para trás!

# Sumário

Neste código, que faz parte do projeto da IX Maratona de TI sobre Reconhecimento Facial com Python e OpenCV, são apresentadas algumas instruções importantes para o desenvolvimento do projeto. O código possui um sumário detalhado, que aborda os seguintes tópicos:

## [Plano de aula](https://github.com/victor-renan/face-recognition/blob/main/PLANO.md)

1. [Verifique se o Python e o pip estão instalados](#1-verifique-se-o-python-e-o-pip-estão-instalados)
2. [Baixe o Iriun Webcam](#2-baixe-o-iriun-webcam)
3. [Baixe os recursos do Github](#3-baixe-os-recursos-do-github)
4. [Uma olhada pelos arquivos baixados](#4-uma-olhada-pelos-arquivos-baixados)
5. [Introdução ao Python](#5-introdução-ao-python)
    1. [Tipos de dados em Python](#51-tipos-de-dados-em-python)
    2. [Operações com listas](#52-operações-com-listas)
    3. [Funções](#53-funções)
    4. [Trabalhando com arquivos de texto](#54-trabalhando-com-arquivos-de-texto)
6. [Introdução ao OpenCV](#6-introdução-ao-opencv)
    1. [Abrindo imagem](#61-abrindo-imagem)
    2. [Abrindo Webcam](#62-abrindo-webcam)
    3. [Criando um CascadeClassifier](#63-criando-um-cascadeclassifier)
    4. [Criando um LBPHRecognizer](#64-criando-um-lbphrecognizer)
7. [Selenium](#7-selenium)
    1. [Usando o webdriver](#71-usando-o-webdriver)
    2. [Abrindo vídeo do Youtube](#72-abrindo-video-do-youtube)
9. [Desafio 1: O Vídeo de Maria](#desafio-1-o-vídeo-de-maria)
10. [Desafio 2: O Banco Central de Araripe](#desafio-2-o-banco-central-de-araripe)
11. [Submissões e Certificado](#submissões-e-certificado)

## 1. Verifique se o Python e o pip estão instalados

Primeiramente, é necessário verificar se o `Python` e o `pip` estão devidamente instalados no seu computador. Entre no `Windows PowerShell` e digite:
```
python --version
```
e depois
```
pip --version
```

*Obs.: Ambos os comandos devem devem retornar uma versão, ex.: Python 3.10.2*

Caso o python não esteja instalado, você pode baixa-lo pelo seguinte link https://www.python.org/ftp/python/3.10.10/python-3.10.10-amd64.exe.

## 2. Baixe o Iriun Webcam

Depois, é necessário ter em seu computador e em seu celular o Iriun Webcam para abrir a câmera no PC. Você pode baixa-los nos links abaixo:
- Para celular: (Play Store) https://play.google.com/store/apps/details?id=com.jacksoftw.webcam&hl=pt_BR&gl=US
- Para desktop: https://1758658189.rsc.cdn77.org/IriunWebcam-2.7.8.exe

## 3. Baixe os recursos do Github

Baixe os aquivos que estão disponibilizados no nosso repositório oficial (https://github.com/victor-renan/face-recognition), clique no botão `Code` depois em `Download Zip`. **Salve na área de trabalho**. Veja abaixo:

![Imagem do download](https://i.imgur.com/gr3ir9J.png)

Depois de baixar, faça a extração do arquivo baixado.

### Abrindo a pasta no VS Code

Em seguida abra o `VS Code` e clique em `File` ou `Arquivo` > `Open Folder` ou `Abrir Pasta` e selecione a pasta `face-recognition-main` que você extraiu.


## 4. Uma olhada pelos arquivos baixados

Quando você extrair a pasta, os seguintes arquivos estarão na pasta:

```
face-recognition
  |--- modelos
  |--- imagens
  |--- automacao.py
  |--- reconhecimento.py
  |--- treinamento.py
  |--- introd.py
  |--- banco.py
  |--- maria.py
  |--- requirements.txt
  ...
```

### reconhecimento.py

Esse é o arquivo principal, onde você escreverá a maior parte do código.

### treinamento.py

Arquivo onde será feito o treinamento.

### imagens

Pasta onde serão colocadas as imagens

### modelos

Pasta onde serão gerados os modelos

### introd.py

Arquivo de introdução a Python

### automacao.py

Arquivo de exemplificação do selenium

### requirements.txt

Esse é o arquivo que contém as bibliotecas que serão instaladas.

### banco.py

Arquivo para o desafio do `Banco Central do Araripe`.

### maria.py

Arquivo para o desafio do `Vídeo de Maria`.

# 5. Introdução ao Python

Python é uma linguagem de programação de alto nível e fácil entendimento. Com sua sintaxe simples, é uma ótima escolha para iniciantes. Python é amplamente utilizado em diversas áreas, como desenvolvimento web, análise de dados e aprendizado de máquina. Sua comunidade ativa e biblioteca abrangente tornam o Python uma opção versátil para criar projetos incríveis.

## 5.1. Tipos de dados em Python

O código abaixo mostra vários exemplos de tipos de dados em Python, como números inteiros, números de ponto flutuante, números complexos, strings, valores booleanos, listas, tuplas, conjuntos, dicionários e o tipo nulo. Cada variável é inicializada com um exemplo de cada tipo de dado e, em seguida, imprime o valor e o tipo de cada variável.

```python
# Tipos numéricos
inteiro = 10            # Número inteiro
ponto_flutuante = 3.14  # Número de ponto flutuante
complexo = 2 + 3j       # Número complexo

# Tipos de texto
string = "Olá, mundo!"   # Sequência de caracteres (string)

# Tipos booleanos
verdadeiro = True       # Valor booleano True (verdadeiro)
falso = False           # Valor booleano False (falso)

# Tipos de sequências
lista = [1, 2, 3]       # Lista (sequência mutável)
tupla = (4, 5, 6)       # Tupla (sequência imutável)
conjunto = {7, 8, 9}    # Conjunto (coleção desordenada de elementos únicos)
dicionario = {'a': 1, 'b': 2}  # Dicionário (mapeamento de chaves para valores)

# Tipo nulo
nulo = None             # Valor especial que indica a ausência de valor

# Imprimindo os valores e tipos de dados
print(f"Valor: {inteiro}, Tipo: {type(inteiro)}")
print(f"Valor: {ponto_flutuante}, Tipo: {type(ponto_flutuante)}")
print(f"Valor: {complexo}, Tipo: {type(complexo)}")
print(f"Valor: {string}, Tipo: {type(string)}")
print(f"Valor: {verdadeiro}, Tipo: {type(verdadeiro)}")
print(f"Valor: {falso}, Tipo: {type(falso)}")
print(f"Valor: {lista}, Tipo: {type(lista)}")
print(f"Valor: {tupla}, Tipo: {type(tupla)}")
print(f"Valor: {conjunto}, Tipo: {type(conjunto)}")
print(f"Valor: {dicionario}, Tipo: {type(dicionario)}")
print(f"Valor: {nulo}, Tipo: {type(nulo)}")
```

## 5.2. Operações com listas

Nesta oficina, utilizaremos várias operações com listas em Python, veja abaixo alguns conceitos que abrangem essas operações:

### 5.2.1. Indexes (Índices)

Em Python, assim como em qualquer outra linguagem, algum elemento de uma lista pode ser referenciado pela sua posição na lista, também chamada de índice. Veja abaixo uma melhor exemplificação:

```python
# Define uma lista
lista = ["Renan", "Ramon", "Aparecido", "Heron", "Nonato"]

# Seleciona um elemendo da lista pelo index (índice)
elemento = lista[3] # Lembre que o primeiro elemento é o 0, então 0=1, 1=2, ...

# Imprime o elemento
print(elemento)

# Saída: "Heron"
```

### 5.2.2. Fatiamento

O código abaixo demonstra como obter a sublista contendo os elementos do índice 0 ao índice 2 (3º elemento excluído) da lista original usando o fatiamento [0:3]. A sublista resultante será uma nova lista contendo os elementos extraídos.

```python
# Definindo a lista original
lista = ["Renan", "Ramon", "Aparecido", "Heron", "Nonato"]

# Exibindo a lista original
print("Lista original: ", lista)

# Obtendo a sublista do índice 0 ao índice 2 (3º elemento excluído)
sublista = lista[0:3]

# Exibindo a sublista resultante
print("Sublista resultante: ", sublista)

# Saída:
# Lista original: ["Renan", "Ramon", "Aparecido", "Heron", "Nonato"]
# Sublista resultante:  ["Renan", "Ramon", "Aparecido"]
```

### 5.2.3. `append()` e `remove()`

Para adicionar e remover itens de uma lista, são utilizados os métodos `append()` e `remove()`, respectivamente. Veja abaixo um código mostrando como funciona:

```python
# Criando uma lista vazia
lista = []

# Utilizando o append para adicionar elementos à lista
lista.append('maçã')
lista.append('banana')
lista.append('laranja')

# Utilizando o remove para remover um elemento da lista
lista.remove('banana')

# Exibindo a lista resultante
print("Lista resultante:", lista)

# Saída:
# Lista resultante: ['maçã', 'laranja']
```

## 5.3. Funções

No Python, as funções são declaradas de um modo bem singular, de forma um pouco diferente das demais linguagens. Veja:

```python
# Definindo uma função que recebe dois números e retorna a soma deles
def somar_numeros(a, b):
    resultado = a + b
    return resultado

# Chamando a função e armazenando o resultado em uma variável
soma = somar_numeros(5, 3)

# Exibindo o resultado da soma
print("Resultado da soma: ", soma)

# Saída:
# Resultado da soma: 8
```

## 5.4. Trabalhando com arquivos de texto

Você também verá algumas situações em que será necessário obter alguns dados a partir de arquivos `.txt` e para isso, o Python oferece alguns recursos interessantíssimos. Veja alguns deles:

### 5.4.1. Convertendo arquivo `.txt` em lista

Para converter cada linha de um arquivo `.txt` em lista, você pode utilizar um dos códigos abaixo:

```python
# Criando uma lista vazia para armazenar as linhas do arquivo
linhas = []

# Abrindo o arquivo de texto em modo de leitura
with open('nome_arquivo.txt', "r") as arquivo:
    # Lendo cada linha do arquivo
    for linha in arquivo:
        # Removendo caracteres de quebra de linha (\n)
        linha = linha.strip()
        # Adicionando a linha à lista
        linhas.append(linha)
        
# Exibindo as linhas armazenadas na lista
for linha in linhas:
    print(linha)

# Saída: ["Linha", "Linha", "Linha", ...]
```
Ou, de maneira mais resumida,
```python
# Abre o arquivo, lê e separa por cada linha
linhas = open('nome_arquivo.txt').read().splitlines()

# Saída: ["Linha", "Linha", "Linha", ...]
```

# 6. Introdução ao OpenCV

O **OpenCV** (*Open Source Computer Vision*) é uma biblioteca popular e de código aberto amplamente utilizada para *processamento de imagens* e *visão computacional*. Ela fornece uma ampla variedade de funções e algoritmos que permitem realizar tarefas como leitura, gravação e processamento de imagens e vídeos.

Com o OpenCV, é possível carregar imagens a partir de arquivos, realizar operações de pré-processamento, como redimensionamento e ajuste de contraste, e aplicar uma variedade de filtros para melhorar a qualidade da imagem. Além disso, a biblioteca permite **detectar e rastrear objetos**, realizar **reconhecimento facial**, extrair **características de imagem**, entre outras tarefas avançadas de visão computacional.

Uma das características mais poderosas do OpenCV é a sua capacidade de trabalhar em tempo real com fluxos de vídeo. Isso significa que você pode aplicar algoritmos de processamento de imagem e visão computacional a partir de uma câmera em tempo real, abrindo um mundo de possibilidades para aplicações como **detecção de objetos em tempo real**, **análise de movimento** e muito mais.

O OpenCV é escrito principalmente em C++, mas possui interfaces para várias linguagens de programação, incluindo Python, Java e C#. Isso torna a biblioteca acessível e utilizável em uma ampla gama de projetos e plataformas.

## 6.1. Abrindo imagem

Para abrir uma imagem usando o OpenCV, você pode seguir os seguintes passos:

1. Primeiro, importe a biblioteca `cv2`.
2. Utilize a função `cv2.imread()` para carregar a imagem desejada. Certifique-se de fornecer o caminho completo para a imagem.
3. Verifique se a imagem foi carregada corretamente.
4. Para exibir a imagem em uma janela, utilize a função `cv2.imshow()`. O primeiro parâmetro é o nome da janela que pode ser personalizado.
5. Aguarde até que uma tecla seja pressionada para fechar a janela usando `cv2.waitKey(0)`.
6. Por fim, feche todas as janelas abertas com `cv2.destroyAllWindows()`.

Veja o exemplo abaixo:

```python
import cv2

# Caminho completo para a imagem
caminho_imagem = "caminho/para/imagem.jpg"

# Carrega a imagem
imagem = cv2.imread(caminho_imagem)

# Verifica se a imagem foi carregada corretamente
if imagem is not None:
    # Exibe a imagem em uma janela
    cv2.imshow("Imagem", imagem)
    # Aguarda até que uma tecla seja pressionada
    cv2.waitKey(0)
    # Fecha a janela
    cv2.destroyAllWindows()
else:
    print("Falha ao carregar a imagem.")
```

## 6.2. Abrindo Webcam

O código abaixo abre a webcam padrão do sistema (geralmente a primeira webcam disponível), utilizando dos mesmos conceitos anteriores. Ele captura cada quadro de vídeo da webcam e exibe em uma janela chamada "Webcam". O loop é interrompido quando a tecla 'q' é pressionada.

```python
import cv2

# Inicializa o objeto de captura de vídeo
captura = cv2.VideoCapture(0)

# Verifica se a webcam foi aberta corretamente
if not captura.isOpened():
    print("Não foi possível abrir a webcam.")
    exit()

# Loop principal para capturar e exibir o vídeo
while True:
    # Captura o próximo quadro da webcam
    ret, quadro = captura.read()

    # Verifica se o quadro foi capturado corretamente
    if not ret:
        print("Falha ao capturar o quadro.")
        break

    # Exibe o quadro em uma janela
    cv2.imshow("Webcam", quadro)

    # Verifica se a tecla 'q' foi pressionada para interromper o loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera o objeto de captura de vídeo e fecha as janelas
captura.release()
cv2.destroyAllWindows()
```

## 6.3. Criando um CascadeClassifier

No código abaixo, você precisa substituir 'caminho/para/o/arquivo.xml' pelo caminho correto para o arquivo XML do classificador que deseja utilizar, como por exemplo o arquivo XML para detecção facial. Certifique-se de ter o OpenCV instalado em seu ambiente Python.

O código irá abrir a webcam, capturar os frames, converter cada frame para escala de cinza e aplicar o classificador para detectar rostos no frame. Em seguida, desenha retângulos ao redor das faces detectadas e exibe o frame resultante em uma janela. O loop continuará até que a tecla 'q' seja pressionada, momento em que a webcam será liberada e as janelas serão fechadas.

```python
import cv2

# Define o caminho para o arquivo XML do classificador
caminho_arquivo_xml = 'caminho/para/o/arquivo.xml'

# Cria um objeto CascadeClassifier
classificador = cv2.CascadeClassifier(caminho_arquivo_xml)

# Verifica se o classificador foi carregado corretamente
if classificador.empty():
    print("Não foi possível carregar o arquivo XML do classificador.")
    exit()

# Inicializa a webcam
webcam = cv2.VideoCapture(0)

# Loop para capturar e exibir os frames da webcam
while True:
    # Captura um frame da webcam
    ret, frame = webcam.read()

    # Converte o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplica o classificador para detecção facial
    faces = classificador.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Desenha um retângulo ao redor das faces detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Exibe o frame resultante
    cv2.imshow('Detector Facial', frame)

    # Verifica se a tecla 'q' foi pressionada para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera os recursos
webcam.release()
cv2.destroyAllWindows()
```

## 6.4. Criando um LBPHRecognizer

O código abaixo mostra uma das maneiras de criar um reconhecedor por LBPH (Local Binary Pattern Histograms).

```python
import cv2
import os
import numpy as np

# Function to load training images
def load_training_images(directory):
    images = []
    labels = []
    for folder_name in os.listdir(directory):
        folder = os.path.join(directory, folder_name)
        if not os.path.isdir(folder):
            continue
        for file_name in os.listdir(folder):
            image = cv2.imread(os.path.join(folder, file_name), cv2.IMREAD_GRAYSCALE)
            images.append(image)
            labels.append(int(folder_name))
    return images, labels

# Load training images
training_directory = 'path/to/training/images'
training_images, training_labels = load_training_images(training_directory)

# Create LBPH Face Recognizer object
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Train the LBPH recognizer with training images
recognizer.train(training_images, np.array(training_labels))

# Function to recognize a face in an image
def recognize_face(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    label, confidence = recognizer.predict(gray_image)
    return label, confidence

# Example usage: recognize a face in an image
test_image = cv2.imread('path/to/test/image')
label, confidence = recognize_face(test_image)
print('Label:', label)
print('Confidence:', confidence)
```

1. Importação das bibliotecas:
   - `import cv2`: Importa a biblioteca OpenCV, que é usada para processamento de imagens e reconhecimento facial.
   - `import os`: Importa a biblioteca os, que fornece funcionalidades para interagir com o sistema operacional.

2. Função `load_training_images`:
   - Carrega as imagens de treinamento e seus respectivos rótulos (labels) de um diretório específico.
   - Percorre os subdiretórios dentro do diretório fornecido, lendo cada imagem e adicionando-a a uma lista de imagens.
   - Também registra o rótulo correspondente a cada imagem na lista de rótulos.

3. Carregamento das imagens de treinamento:
   - Define o diretório que contém as imagens de treinamento.
   - Chama a função `load_training_images` para carregar as imagens e rótulos de treinamento a partir do diretório.

4. Criação do objeto LBPH Face Recognizer:
   - Utiliza a função `cv2.face.LBPHFaceRecognizer_create()` para criar um objeto reconhecedor LBPH.

5. Treinamento do reconhecedor LBPH:
   - Utiliza o método `train` do objeto reconhecedor, passando as imagens de treinamento e seus rótulos.
   - O reconhecedor é treinado para aprender a reconhecer os rostos correspondentes a cada rótulo.

6. Função `recognize_face`:
   - Recebe uma imagem como entrada.
   - Converte a imagem em escala de cinza.
   - Utiliza o método `predict` do objeto reconhecedor para reconhecer o rótulo e a confiança do rosto presente na imagem.

7. Reconhecimento de uma face em uma imagem de teste:
   - Carrega uma imagem de teste específica.
   - Chama a função `recognize_face` para reconhecer o rosto presente na imagem.
   - Imprime o rótulo e a confiança associados ao rosto reconhecido.

Certifique-se de substituir os caminhos das imagens de treinamento e da imagem de teste pelos caminhos reais correspondentes ao seu ambiente.


# 7. Selenium

O Selenium é uma biblioteca popular de automação de testes e interação com navegadores web. Ele fornece uma interface para controlar e interagir com navegadores web de forma programática, permitindo a automatização de tarefas repetitivas, a realização de testes automatizados em páginas da web e a extração de dados de sites.

Com o Selenium, é possível desenvolver scripts em diversas linguagens de programação, incluindo Python, Java, C#, entre outras. Ele oferece recursos para localizar e manipular elementos da página, preencher formulários, clicar em botões, realizar ações de rolagem, capturar screenshots, além de possibilitar a execução de comandos JavaScript no contexto da página.

# 7.1. Usando o webdriver

O Selenium WebDriver é uma parte fundamental do Selenium, que fornece uma API de alto nível para interagir com navegadores web. Ele é responsável por controlar o navegador de forma programática e executar ações como clicar em elementos, preencher formulários, enviar requisições, aguardar por elementos na página e capturar informações. Veja o exemplo a seguir onde o GitHub é aberto:

```python
# Importando as bibliotecas necessárias
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Inicializando o driver do Selenium
driver = webdriver.Chrome()

# Acessando um site
driver.get("https://github.com")

# Interagindo com elementos da página
campo_busca = driver.find_element_by_name("q")  # Localiza o campo de busca
campo_busca.send_keys("Selenium Python")  # Insere o termo de busca
campo_busca.send_keys(Keys.RETURN)  # Simula a tecla Enter
```

# 7.2. Abrindo Video do Youtube
Abaixo, está um código de como abrir um vídeo do Youtube com o `Selenium` e interagir com o mesmo:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializando o driver do Selenium
driver = webdriver.Chrome()

# Acessando o YouTube
driver.get("https://www.youtube.com/video")

# Aguardando o vídeo carregar
time.sleep(5)  # Pausa de 5 segundos para o vídeo carregar (ajuste conforme necessário)

# Pausando o vídeo pressionando a tecla de espaço
body = driver.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.SPACE)

# Aguardando 3 segundos
time.sleep(3)

# Despausando o vídeo pressionando a tecla de espaço novamente
body.send_keys(Keys.SPACE)

# Aguardando mais 5 segundos antes de fechar o navegador
time.sleep(5)

# Fechando o navegador
driver.quit()
```

# Desafio 1: O Vídeo de Maria

Maria está com um sério problema: sua mãe a chama a cada instante e ela precisa ficar pausando um vídeo que ela está assistindo. Como ela estava com muita preguiça, decidiu implantar um sistema de reconhecimentofacial para pausar o video sempre que ela não estiver na frente do computador, e dar play sempre que ela estiver.Como maria pode fazer isso?

Link do vídeo: `https://www.youtube.com/watch?v=WWn4lfNQy2s`

**Boa sorte!**

# Desafio 2: O Banco Central de Araripe

O gerente do Banco Central do Araripe está enfrentando problemas de velocidade e queria mudar o sistema de autenticação do seu sistema da maneira clássica para a detecção facial. Como ele poderia fazer isso?

**Boa Sorte!**

# Submissões e certificado

Submeta suas respostas para esses desafios no site https://facerecogpyocv.vercel.app/

Crie uma conta, caso não tenha, e teste suas resoluções. Caso passe nos testes, você está apto a receber um certificado de conclusão verificado e totalmente digital, semelhante ao que está a seguir:

![Imagem do Cert](https://i.imgur.com/Nby4mE8.png)
