'''
    Desafio 2: O Banco Central do Araripe

    O gerente do Banco Central do Araripe está enfrentando
    problemas de velocidade e queria mudar o
    sistema de autenticação do seu sistema da maneira clássica
    para a detecção facial. Como ele poderia fazer isso?

    Dica: Você precisa modificar uma parte X desse código
    Escreva seu código abaixo deste comentário.

    Boa sorte!
'''

import PySimpleGUI as sg
import random
import base64

# banco de dados ficticio
db = [
    {"username": "jose", "password": "jose123"},
    {"username": "maria", "password": "maria123"},
]

# define o tema
sg.theme("Dark Amber")

# define a tela de login
username_id = '-username-'
password_id = '-password-'
submit_id = 'Enviar'
login = [
    [sg.Push(), sg.Text("Seja bem vindo ao sistema do Banco Central do Araripe!",
                        font=('Monospace', 14)), sg.Push()],
    [sg.HSeparator()],
    [sg.VPush()],
    [sg.Push(), sg.Text("Digite seu username:"), sg.Push()],
    [sg.Push(), sg.InputText(key=username_id), sg.Push()],
    [sg.Push(), sg.Text("Digite sua senha:"), sg.Push()],
    [sg.Push(), sg.InputText(key=password_id), sg.Push()],
    [sg.Push(), sg.Submit(submit_id), sg.Push()],
    [sg.VPush()],
]

# define a tela de transacoes
mline_id = '-mline-'
transactions = [
    [sg.Text("Transactions")],
    [sg.HSeparator()],
    [sg.MLine(size=(80, 30), key=mline_id)],
    [sg.Submit()],
]

# define uma janela com a tela de login
window = sg.Window("Banco Central do Araripe", login, size=(640, 480))

# acha todos os usuarios


def find_all():
    usernames = []
    for item in db:
        usernames.append(item["username"])

    return usernames


# Gera dados aleatorios
def generate_data(multiline, multiline_value):
    multiline.update(
        multiline_value + "\n" +
        f"{random.randint(1, 1000)}-->{base64.b64encode(random.randbytes(100))} <-> \n")


# autentica um usuario
def autentica(username, password):
    if username in find_all():
        if password == db[find_all().index(username)]["password"]:
            window = sg.Window(
                f"{username} -> (ADMIN) Banco Central do Araripe", transactions)

            while True:
                event, values = window.read()

                if event == "Submit":
                    generate_data(window[mline_id], values[mline_id])

                if event in (sg.WIN_CLOSED, 'Exit'):
                    break

        else:
            sg.Popup("Senha incorreta!")

    else:
        sg.Popup("Este usuário não existe!")


# loop da janela
while True:
    event, values = window.read()

    if event == submit_id:
        autentica(values[username_id], values[password_id])
        break

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    window.close()
