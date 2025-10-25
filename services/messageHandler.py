from models.message import Message
from db.connection import DBConnection
from models.user import User
from models.crypto import Crypto

class MessageHandler:
    def __init__(self):
        db = DBConnection()
        self.messages = db.getCollection("Messages")

    def sendMessage(self, sender: str) -> str:
        recipient = input("Para quem deseja enviar a mensagem?\nDestinatário: ")
        message = input("Digite a mensagem: (min. 50 caractares): ").encode()
        secretKey = input("Digite a chave secreta: ").encode()

        mensagemCriptografada = Crypto.encrypt(secretKey, message)
        print("Criptografada:", mensagemCriptografada)

        new_message = Message(sender, recipient, "sent", mensagemCriptografada)
        self.messages.insert_one(new_message.toDict())
        return "Mensagem enviada com sucesso!"
