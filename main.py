from services.auth import AuthService
from models.crypto import Crypto
from services.session import userSession
import os

def main():
    auth = AuthService()
    
    while True:
        print("\n=== BEM-VINDO A MESSAGERIA SEGURA ===")
        print("1 - Registrar")
        print("2 - Logar")
        print("0 - Sair")

        opcao = input("Escolha: ")
        print("=======================")

        if opcao == "1":
            username = input("Usuário: ")
            password = input("Senha: ")
            print(auth.registrar(username, password))
            os.system('cls')
        elif opcao == "2":
            username = input("Usuário: ")
            password = input("Senha: ")
            ok, user, msg = auth.logar(username, password)
            print(msg)
            if ok:
                os.system('cls')
                userSession(user)

        elif opcao == "0":
            os.system('cls')
            print("Saindo...")
            break
        else:
            os.system('cls')
            print("Opção inválida.")

if __name__ == "__main__":
    main()


#    senha = "senha".encode()
#    mensagem = "mensagem para ser criptografada".encode()
#    senha2 = "alalala".encode()

#    mensagem_criptografada = Crypto.encrypt(senha, mensagem)
#    print("Criptografada:", mensagem_criptografada)

#    mensagem_decriptografada = Crypto.decrypt(senha, mensagem_criptografada)
#    print("Decriptografada:", mensagem_decriptografada.decode())