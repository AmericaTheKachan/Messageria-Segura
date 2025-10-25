from db.connection import DBConnection
from models.user import User

class AuthService:
    def __init__(self):
        db = DBConnection()
        self.users = db.getCollection("Users")

    def registrar(self, username: str, password: str) -> str:
        if self.users.find_one({"username": username}):
            return "Usuário indísponivel."
        new_user = User(username, password)
        self.users.insert_one(new_user.toDict())
        return "Usuário cadastrado com sucesso!"
    
    def logar(self, username: str, password: str):
        user = self.users.find_one({"username": username})
        if not user:
            return False, "Usuário não encontrado."
        
        if User.verifyPassword(user["password"], user["salt"], password):
            print("UserAuth: ", user)
            return True, user ,f"Bem-vindo de volta, {username}!"
        else:
            return False, "Senha incorreta."