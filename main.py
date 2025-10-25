from services.auth import AuthService

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
