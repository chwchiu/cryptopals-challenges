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

def decrypt_aes_128_CBC(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    ct_blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    
    pt = b""
    prev_ct = iv
    for block in ct_blocks:
        pt += xor_bytestrs(decrypt_aes_128_ecb(block, key), prev_ct)
        prev_ct = block
    
    return pt

def encrypt_aes_128_CBC(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    pt_blocks = [plaintext[i:i+16] for i in range(0, len(plaintext), 16)]
    
    ct = b""
    prev_ct = iv
    for block in pt_blocks:
        encrypted_block = encrypt_aes_128_ecb(xor_bytestrs(block, prev_ct), key)
        ct += encrypted_block
        prev_ct = encrypted_block
    
    return ct

def pkcs7_padding(plaintext: bytes, blocksize: int) -> bytes:
    padding_required = blocksize - (len(plaintext) % blocksize)
    padding = bytes([padding_required]) * padding_required
    
    return plaintext + padding

def xor_bytestrs(bstr1: bytes, bstr2: bytes) -> bytes: 
    return bytes([b ^ bstr2[i] for i, b in enumerate(bstr1)])