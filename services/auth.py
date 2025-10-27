from db.connection import DBConnection
from models.user import User

class AuthService:
    def __init__(self):
        db = DBConnection()
        self.users = db.getCollection("Users")

    def registrar(self, username: str, password: str) -> str:
        if self.users.find_one({"username": username}):
            return "\033[31mErro: Usuário indísponivel.\033[m"
        new_user = User(username, password)
        self.users.insert_one(new_user.toDict())
        return "\033[32mSucesso: Usuário cadastrado com sucesso!\033[m"
    
    def logar(self, username: str, password: str):
        user = self.users.find_one({"username": username})
        if not user:
            return False, "User not found", "\033[31mErro: Usuário ou senha incorretos.\033[m"
        
        if User.verifyPassword(user["password"], user["salt"], password):
            return True, user ,f"\033[32mSucesso: Bem-vindo de volta, {username}!\033[m"
        else:
            return False, "User not found", "\033[31mErro: Usuário ou senha incorretos.\033[m"