'''
    Desafio 2: O Banco Central do Araripe

    O gerente do Banco Central do Araripe está enfrentando
    problemas de velocidade e queria mudar o
    sistema de autenticação do seu sistema da maneira clássica
    para a detecção facial. Como ele poderia fazer isso?

    Dica: Você precisa modificar uma parte X desse código
    Escreva seu código abaixo deste comentário.

    Lembre-se: para executar este arquivo, digite:

    ----------------------------------------------
    python banco.py
    ----------------------------------------------

    Boa sorte!
'''

# Banco de dados fictício
db = [
    {
        "username": "ana",
        "password": "ana123",
    },
    {
        "username": "bia",
        "password": "bia123",
    },
]

# Func. que autentica os usuarios
def autentica(username, password):
    usernames = [item["username"] for item in db]

    if username in usernames:
        if password == db[usernames.index(username)]["password"]:
            print("Autenticado!")
            return True
        else:
            print("Senha incorreta!")
            return False
    else:
        print("Usuário não existe!")
        

# SISTEMA ANTIGO
username = str(input("Digite seu username: "))
password = str(input("Digite sua password: "))


autentica(username, password)