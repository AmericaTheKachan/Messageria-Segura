from models.user import User
from services.messageHandler import MessageHandler
import os

def userSession(user: User):

    msgHandler = MessageHandler()

    while True:
        print(f"\n=== BEM-VINDO, {user["username"]} ===")
        print("1 - Enviar Mensagem")
        print("0 - Desconectar")

        opcao = input("Escolha: ")

        if opcao == "1":
            os.system('cls')
            print(msgHandler.sendMessage(user["username"]))
        elif opcao == "0":
            os.system('cls')
            print("Desconectando...")
            break
        else:
            print("Opção inválida.")