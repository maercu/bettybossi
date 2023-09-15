from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import hashlib
import base64


def encrypt(key, iv, text):
    text = text.encode()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(text, AES.block_size))
 

def decrypt(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), AES.block_size).decode()


if __name__ == "__main__":
    iv = get_random_bytes(16)
    password = "somePasswordOfAnySize"
    key = hashlib.sha256(password.encode()).digest()
    # or static key of 16 bytes
    #key = "0123456789abcdef".encode()
    text = "1234567890123456"

    ciphertext = encrypt(key, iv, text)
    print(f"ciphertext in bytes: {ciphertext}")
    print(f"ciphertext in hex: {base64.b16encode(ciphertext).decode().lower()}")

    plaintext = decrypt(key, iv, ciphertext)
    print(f"plaintext after decryption: {plaintext}")