from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64
import os

class Crypto:
    SALT_SIZE = 16

    @classmethod
    def kdf(cls, senha: bytes, salt: bytes ) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations= 900_000,
        )

        return base64.urlsafe_b64encode(kdf.derive(senha))
    
    @classmethod
    def encrypt(cls, password: bytes, msg: bytes) -> bytes:

        salt = os.urandom(cls.SALT_SIZE)
        key = cls.kdf(password,salt)
        fernet = Fernet(key)
        token = fernet.encrypt(msg)
        return salt + token
    
    @classmethod
    def decrypt(cls, password: bytes, msgCrypt: bytes) -> bytes:
        salt = msgCrypt[:cls.SALT_SIZE]
        token = msgCrypt[cls.SALT_SIZE:]
        key = cls.kdf(password, salt)
        fernet = Fernet(key)

        try:
            msgDecrypt = fernet.decrypt(token)
        except Exception:
            
            msgDecrypt = base64.urlsafe_b64encode(token)

        return msgDecrypt