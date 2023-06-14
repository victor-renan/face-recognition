# IX Maratona de TI: Reconhecimento Facial com Python e OpenCV

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8.svg?style=for-the-badge&logo=OpenCV&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A.svg?style=for-the-badge&logo=Selenium&logoColor=white)

![Python e OpenCV](https://i.imgur.com/8yxaomz.png)

Seja bem vindo a oficina Reconhecimento Facial com Python e OpenCV! Abaixo estão algumas instruções que serão importantíssimas no decorrer do seu projeto. Preste bastante atenção nos comandos dos instrutores para que você não se perda nem fique para trás!

# Sumário

Neste código, que faz parte do projeto da IX Maratona de TI sobre Reconhecimento Facial com Python e OpenCV, são apresentadas algumas instruções importantes para o desenvolvimento do projeto. O código possui um sumário detalhado, que aborda os seguintes tópicos:

1. [Verifique se o Python e o pip estão instalados](#1-verifique-se-o-python-e-o-pip-estão-instalados)
2. [Baixe o Iriun Webcam](#2-baixe-o-iriun-webcam)
3. [Baixe os recursos do Github](#3-baixe-os-recursos-do-github)
4. [Uma olhada pelos arquivos baixados](#4-uma-olhada-pelos-arquivos-baixados)
5. [Introdução ao Python](#5-introdução-ao-python)
    1. [Tipos de dados em Python](#51-tipos-de-dados-em-python)
    2. [Operações com listas](#52-operações-com-listas)
    3. [Funções](#53-funções)
    4. [Trabalhando com arquivos de texto](#54-trabalhando-com-arquivos-de-texto)
6. [Desafio 1: O Vídeo de Maria](#desafio-1-o-vídeo-de-maria)
7. [Desafio 2: O Banco Central de Araripe](#desafio-2-o-banco-central-de-araripe)

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

Caso o python não esteja instalado, você pode baixa-lo pelo seguinte link (https://www.python.org/ftp/python/3.10.10/python-3.10.10-amd64.exe).

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
  |--- .gitignore
  |--- automacao.py
  |--- reconhecimento.py
  |--- treinamento.py
  |--- introd.py
  |--- banco.py
  |--- maria.py
  |--- requirements.txt
  |--- README.md
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

# Desafio 1: O Vídeo de Maria

Maria está com um sério problema: sua mãe a chama a cada instante e ela precisa ficar pausando um vídeo que ela está assistindo. Como ela estava com muita preguiça, decidiu implantar um sistema de reconhecimentofacial para pausar o video sempre que ela não estiver na frente do computador, e dar play sempre que ela estiver.Como maria pode fazer isso?

Link do vídeo: `https://www.youtube.com/watch?v=WWn4lfNQy2s`

**Boa sorte!**

# Desafio 2: O Banco Central de Araripe

O gerente do Banco Central do Araripe está enfrentando problemas de velocidade e queria mudar o sistema de autenticação do seu sistema da maneira clássica para a detecção facial. Como ele poderia fazer isso?

**Boa Sorte!**
