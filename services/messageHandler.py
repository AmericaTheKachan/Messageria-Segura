from models.message import Message
from db.connection import DBConnection
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

    # Puxar mensagens para quem é o destinatario e tem o status como "sent", mensagens são listadas como: (from User, dia e hora)
    # usuário escolhe qual quer ler, depois de escolher pede a chave secreta e mostra a mensagem se estiver certo e coloca o status como "sent". 


    def listMessages(self, user: str):
        mensagens = self.messages.find({"to_user": user, "status": "sent"}).sort("sentDate", -1)

        i = 0
        dict = {}
        for msg in mensagens:
            i += 1
            print(f"{i} - From: {msg['from_user']}, {msg['sentDate']}")
            dict[i] = msg["_id"]
        
        opcao = int(input("Para volta digite 0\nSelecione a mensagem: "))
        if opcao == 0:
            os.system('cls')
            return
        else:
            msgEscolhida = self.messages.find_one({"_id": dict[opcao]})
        
        chaveSecreta = input("Digite a chave MEGA secreta: ").encode()

        mensagemDecifrada = Crypto.decrypt(chaveSecreta, msgEscolhida['message'])
        print(f"Mensagem: {mensagemDecifrada.decode()}")

        self.messages.update_one({"_id": msgEscolhida["_id"]},{"$set": {"status": "seen"}})
