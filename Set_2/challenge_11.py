from ..common_utils import read_file
from ..crypto_utils import encrypt_aes_128_ecb, encrypt_aes_128_CBC, pkcs7_padding
import os
import random

def hex_decode_to_byte(hex: str) -> list[bytes]:
    return bytes.fromhex(hex)

def split_bytestring_16(data: bytes) -> list[bytes]:
    return [data[i: i + 16] for i in range (0, len(data), 16)]

def find_duplicates(data: list[bytes]) -> bool:
    return len(data) != len(set(data))

def random_key_gen(length: int) -> bytes:
    return os.urandom(length)

def random_encryption_scheme(input: bytes) -> tuple[str, bytes]:
    key = random_key_gen(16)
    padding_left = os.urandom(random.randint(5,10))
    padding_right = os.urandom(random.randint(5,10))

    encryption_scheme = random.randint(1,2)
    pt = pkcs7_padding(padding_left + input + padding_right, 16)
    match encryption_scheme:
        case 1:
            # Using ECB
            ct = encrypt_aes_128_ecb(pt, key)
            scheme = "ECB"
        case 2: 
            # Using CBC
            ct = encrypt_aes_128_CBC(pt, key, random_key_gen(16))
            scheme = "CBC"

    return scheme, ct

def encryption_oracle(ct: bytes) -> str:
    bytestring_16 = split_bytestring_16(ct)
    return "ECB" if find_duplicates(bytestring_16) else "CBC"
    

def main(): 
    msg = b"Yellow SubmarineTwo One Nine TwoYellow Submarine" * 2
    scheme, ct = random_encryption_scheme(msg)

    print(f"The CT used {scheme}, and the encryption oracle detected {encryption_oracle(ct)}")


if __name__ == "__main__":
    main()