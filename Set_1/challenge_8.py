from challenge_4 import read_file
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

def hex_decode_to_byte(hex: str) -> list[bytes]:
    return bytes.fromhex(hex)

def split_bytestring_16(data: bytes) -> list[bytes]:
    return [data[i: i + 16] for i in range (0, len(data), 16)]

def find_duplicates(data: list[bytes]) -> bool:
    return len(data) != len(set(data))

def main(): 
    filename = "challenge_8.txt"
    encoded_ciphertexts = read_file(filename)
    for ciphertext in encoded_ciphertexts:
        bytestring = hex_decode_to_byte(ciphertext)
        bytestring_16 = split_bytestring_16(bytestring)

        if find_duplicates(bytestring_16):
            print(f"The following ciphertext: {ciphertext} is likely to have been encrypted with AES ECB")


if __name__ == "__main__":
    main()