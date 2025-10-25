import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


class Crypto:
    def __init__(self, iterations: int = 200_000, salt_size: int = 16):
        self.iterations = iterations
        self.salt_size = salt_size
        self.backend = default_backend()

    def _derive_key(self, password: bytes, salt: bytes) -> bytes:
      
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=self.iterations,
            backend=self.backend
        )
        return kdf.derive(password)

    def encrypt(self, message: str, password: str) -> bytes:
        
        salt = os.urandom(self.salt_size)
        key = self._derive_key(password.encode('utf-8'), salt)
        iv = os.urandom(16)

        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=self.backend)
        encryptor = cipher.encryptor()

        plaintext_bytes = message.encode('utf-8')
        ciphertext = encryptor.update(plaintext_bytes) + encryptor.finalize()

        payload = salt + iv + ciphertext
        return base64.b64encode(payload)

    def decrypt(self, token_b64: bytes, password: str) -> str:
        
        try:
            data = base64.b64decode(token_b64)
        except Exception:
            data = token_b64

        if len(data) < (self.salt_size + 16):
            return "❌ Mensagem cifrada inválida/curta."

        salt = data[:self.salt_size]
        iv = data[self.salt_size:self.salt_size + 16]
        ciphertext = data[self.salt_size + 16:]

        key = self._derive_key(password.encode('utf-8'), salt)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=self.backend)
        decryptor = cipher.decryptor()

        plaintext_bytes = decryptor.update(ciphertext) + decryptor.finalize()
        return plaintext_bytes.decode('utf-8', errors='replace')
