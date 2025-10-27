from services.messageHandler import MessageHandler
from models.user import User
import os

def userSession(user: User):

    msgHandler = MessageHandler()

    while True:
        print(f"\n=== BEM-VINDO, {user["username"]} ===")
        print("1 - Enviar Mensagem")
        print("2 - Ler novas mensagens")
        print("0 - Desconectar")

        opcao = input("Escolha: ")

        if opcao == "1":
            os.system('cls')
            print(msgHandler.sendMessage(user["username"]))
        elif opcao == "2":
            os.system('cls')
            msgHandler.listMessages(user["username"])
            os.system('cls')
        elif opcao == "0":
            os.system('cls')
            print("\033[33mAviso: Desconectando...\033[m")
            break
        else:
            os.system('cls')
            print("\033[31mErro: Opção inválida.\033[m")