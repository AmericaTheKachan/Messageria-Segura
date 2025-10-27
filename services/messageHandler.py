from db.connection import DBConnection
from models.message import Message
from models.crypto import Crypto
import datetime
import os

class MessageHandler:
    def __init__(self):
        db = DBConnection()
        self.messages = db.getCollection("Messages")

    def sendMessage(self, sender: str) -> str:
        print("\033[33mAviso: Para cancelar, digite CANCELAR em qualquer campo.\033[m")
        recipient = input("Para quem deseja enviar a mensagem?\nDestinatário: ")
        if recipient.lower() == "cancelar":
            os.system('cls')
            return "\033[33mAviso: Operação cancelada\033[m"
        message = ""
        while(len(message) < 50):
            message = input("Digite a mensagem: (min. 50 caractares): ").encode()
            if message.decode().lower() == "cancelar":
                os.system('cls')
                return "\033[33mAviso: Operação cancelada\033[m"
            if len(message) < 50:
                os.system('cls')
                print("\033[33mAviso: Para cancelar, digite cancelar em qualquer campo.\033[m")
                print("\033[31mErro: Mensagem deve conter ao menos 50 caracteres.\033[m")
        secretKey = input("Digite a chave secreta: ").encode()
        os.system('cls')
        if secretKey.lower() == "cancelar":
            return "\033[33mAviso: Operação cancelada\033[m"

        mensagemCriptografada = Crypto.encrypt(secretKey, message)

        dataAtual = datetime.datetime.now()

        new_message = Message(sender, recipient, "sent", mensagemCriptografada, dataAtual)
        self.messages.insert_one(new_message.toDict())
        return "\033[32mSucesso: Mensagem enviada com sucesso!\033[m"


    def listMessages(self, user: str):
        mensagens = self.messages.find({"to_user": user, "status": "sent"}).sort("sentDate", -1)

        i = 0
        dict = {}
        for msg in mensagens:
            i += 1
            print(f"{i} - From: {msg['from_user']}, {msg["sentDate"].strftime("%d/%m %H:%M")}")
            dict[i] = msg["_id"]
        
        opcao = int(input("\033[33mAviso: Para voltar digite 0.\033[m\nSelecione a mensagem: "))
        if opcao == 0:
            os.system('cls')
            return
        else:
            msgEscolhida = self.messages.find_one({"_id": dict[opcao]})
        
        chaveSecreta = input("Digite a chave MEGA secreta: ").encode()
        os.system('cls')
        mensagemDecifrada = Crypto.decrypt(chaveSecreta, msgEscolhida['message'])
        print(f"From: {msgEscolhida['from_user']}, {msgEscolhida['sentDate'].strftime("%d/%m %H:%M")}\nMensagem: {mensagemDecifrada.decode()}")
        print("=============================================")
        print("A chave MEGA secreta que você digitou está correta?")
        print("1 - Sim")
        print("2 - Não")
        opcao = input("Escolha: ")
        if opcao == "1":
            dataAtual = datetime.datetime.now()
            self.messages.update_one({"_id": msgEscolhida["_id"]}, {"$set": {"status": "seen", "seen_at": dataAtual}})
        else:
            return

