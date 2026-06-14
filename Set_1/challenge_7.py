from challenge_4 import read_file
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

def main(): 
    filename = "challenge_7.txt"
    ciphertext = "".join(read_file(filename))
    b64_decoded_ciphertext = base64.b64decode(ciphertext)

    key = b'YELLOW SUBMARINE'
    
    plaintext = decrypt_aes_128_ecb(b64_decoded_ciphertext, key)
    print(plaintext)


if __name__ == "__main__":
    main()