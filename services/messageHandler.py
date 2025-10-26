from models.message import Message
from db.connection import DBConnection
from models.user import User
from models.crypto import Crypto
import datetime
import os

class MessageHandler:
    def __init__(self):
        db = DBConnection()
        self.messages = db.getCollection("Messages")

    def sendMessage(self, sender: str) -> str:
        recipient = input("Para quem deseja enviar a mensagem?\nDestinatário: ")
        os.system('cls')
        message = ""
        while(len(message) < 50):
            message = input("Digite a mensagem: (min. 50 caractares): ").encode()
            os.system('cls')
            if len(message) < 50:
                print("Erro: Mensagem deve conter ao menos 50 caracteres.")
            
        secretKey = input("Digite a chave secreta: ").encode()
        os.system('cls')

        mensagemCriptografada = Crypto.encrypt(secretKey, message)

        dataAtual = datetime.datetime.now()

        new_message = Message(sender, recipient, "sent", mensagemCriptografada, dataAtual)
        self.messages.insert_one(new_message.toDict())
        return "Mensagem enviada com sucesso!"
