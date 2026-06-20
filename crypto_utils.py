from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

def decrypt_aes_128_ecb(ciphertext: bytes, key: bytes) -> bytes:
    cipher = Cipher(
        algorithms.AES(key),
        modes.ECB(),
        backend=default_backend()
    )

    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext

def encrypt_aes_128_ecb(plaintext: bytes, key: bytes) -> bytes:
    cipher = Cipher(
        algorithms.AES(key),
        modes.ECB(),
        backend=default_backend(),
    )

    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return ciphertext

def pkcs7_padding(plaintext: bytes, blocksize: int) -> bytes:
    padding_required = blocksize - (len(plaintext) % blocksize)
    padding = bytes([padding_required]) * padding_required
    
    return plaintext + padding

def xor_bytestrs(bstr1: bytes, bstr2: bytes) -> bytes: 
    return bytes([b ^ bstr2[i] for i, b in enumerate(bstr1)])