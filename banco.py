import PySimpleGUI as sg
import time
import math
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
login = [
    [sg.Push(), sg.Text("Seja bem vindo ao sistema do Banco Central do Araripe!", font=('Monospace', 14)), sg.Push()],
    [sg.HSeparator()],
    [sg.VPush()],
    [sg.Push(), sg.Text("Digite seu username:"), sg.Push()],
    [sg.Push(), sg.InputText(key=username_id), sg.Push()],
    [sg.Push(), sg.Text("Digite sua senha:"), sg.Push()],
    [sg.Push(), sg.InputText(key=password_id), sg.Push()],
    [sg.Push(), sg.Submit(), sg.Push()],
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

# loop da janela
while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    def find_all():
        usernames = []
        for item in db:
            usernames.append(item["username"])

        return usernames
    
    if values[username_id] in find_all():
        if values[password_id] == db[find_all().index(values[username_id])]["password"]:
            window2 = sg.Window(f"{values[username_id]} -> (ADMIN) Banco Central do Araripe", transactions)
            
            while True:
                event2, values2 = window2.read()

                def generate_data():
                    window2[mline_id].update(
                        values2[mline_id] + "\n" +
                        f"{random.randint(1, 1000)}-->{base64.b64encode(random.randbytes(100))} <-> \n")

                print(event2)

                if event2 == "Submit":
                    generate_data()

                if event2 in (sg.WIN_CLOSED, 'Exit'):
                    break


        else:
            sg.Popup("Senha incorreta!")

    else:
        sg.Popup("Este usuário não existe!")

    window.close()