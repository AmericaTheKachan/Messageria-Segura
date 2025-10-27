from services.session import userSession
from services.auth import AuthService
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
            os.system('cls')
            print("\033[33mAviso: Para voltar deixe o Usuário e Senha em branco.\033[m")
            username = input("Usuário: ")
            password = input("Senha: ")
            os.system('cls')
            if username and password:
                print(auth.registrar(username, password)) 
        elif opcao == "2":
            os.system('cls')
            print("\033[33mAviso: Para voltar deixe o Usuário e Senha em branco.\033[m")
            username = input("Usuário: ")
            password = input("Senha: ")
            os.system('cls')
            if username and password:
                ok, user, msg = auth.logar(username, password)
                print(msg)
                if ok:
                    userSession(user)

        elif opcao == "0":
            os.system('cls')
            print("\033[33mAviso: Saindo...\033[m") 
            break
        else:
            os.system('cls')
            print("\033[31mErro: Opção inválida.\033[m")

main()

# Metodo de criptografia da mensagem:
# senha = "senha".encode()
# mensagem = "mensagem para ser criptografada".encode()

# mensagem_criptografada = Crypto.encrypt(senha, mensagem)
# print("Criptografada:", mensagem_criptografada)

# mensagem_decriptografada = Crypto.decrypt(senha, mensagem_criptografada)
# print("Decriptografada:", mensagem_decriptografada.decode())