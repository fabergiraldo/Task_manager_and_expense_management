import hashlib;
import os;
from Crypto.Cipher import AES;
import base64;

class EncriptarAES:
    # Genera una clave de 32 bytes a partir de un string
    secretKey = hashlib.sha256(b'YourSecretKey').digest()  # Esto garantiza 32 bytes exactos
    nonce_fijo = b'0123456789ABCDEF'  # Nonce estático de 16 bytes

    @staticmethod
    def cifrar(valor: str) -> str:
        if not valor:
            return ""

        valor_bytes = str.encode(valor)
        cipher = AES.new(EncriptarAES.secretKey, AES.MODE_GCM, nonce=EncriptarAES.nonce_fijo)
        ciphertext, tag = cipher.encrypt_and_digest(valor_bytes)
        encrypted_data = tag + ciphertext
        return base64.b64encode(encrypted_data).decode('utf-8')

    @staticmethod
    def decifrar(valor: str) -> str:
        if not valor:
            return ""

        try:
            encrypted_data = base64.b64decode(valor)
            tag = encrypted_data[:16]
            ciphertext = encrypted_data[16:]

            cipher = AES.new(EncriptarAES.secretKey, AES.MODE_GCM, nonce=EncriptarAES.nonce_fijo)
            plaintext = cipher.decrypt_and_verify(ciphertext, tag)
            return plaintext.decode('utf-8')
        except Exception as e:
            print(f"Error decrypting: {str(e)}")
            return ""