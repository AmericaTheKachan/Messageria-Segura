from services.auth import AuthService
from models.crypto import Crypto

def main():
    auth = AuthService()
    
    while True:
        print("\n=== BEM-VINDO A MESSAGERIA SEGURA ===")
        print("1 - Registrar")
        print("2 - Logar")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            username = input("Usuário: ")
            password = input("Senha: ")
            print(auth.registrar(username, password))
        elif opcao == "2":
            username = input("Usuário: ")
            password = input("Senha: ")
            ok, msg = auth.logar(username, password)
            print(msg)
            if ok:
                break
        elif opcao == "3":
            print("Saindo...")
            break
        else:
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


