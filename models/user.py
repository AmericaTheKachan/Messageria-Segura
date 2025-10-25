from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64
import os

class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash, self.salt = self.hashPassword(password)

    @staticmethod
    def hashPassword(password: str):
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100_000,
        )
        key = kdf.derive(password.encode())
        
        return base64.b64encode(key).decode(), base64.b64encode(salt).decode()
    
    @staticmethod
    def verifyPassword(hash: str, salt: str, password: str) -> bool:
        try:
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=base64.b64decode(salt),
                iterations=100_000,
            )
            kdf.verify(password.encode(), base64.b64decode(hash))
            return True
        except:
            return False
    
    def toDict(self):
        return {
            "username": self.username,
            "password": self.password_hash,
            "salt": self.salt
        }