from ..common_utils import read_file
from ..crypto_utils import encrypt_aes_128_ecb, decrypt_aes_128_ecb, pkcs7_padding, xor_bytestrs
import base64

def split_bytestring_16(data: bytes) -> list[bytes]:
    return [data[i: i + 16] for i in range (0, len(data), 16)]

def decrypt_CBC(ct_blocks: list[bytes], key: bytes, iv: bytes) -> list[bytes]:
    pt = b""

    for i, block in enumerate(ct_blocks):
        if i == 0:
            pt += xor_bytestrs(decrypt_aes_128_ecb(block, key), iv)
        else:
            pt += xor_bytestrs(decrypt_aes_128_ecb(block, key), ct_blocks[i-1])
    
    return pt


def main(): 
    key = b"YELLOW SUBMARINE"
    iv = b"\x00" * 16
    filename = "cryptopals-challenges/Set_2/challenge_10.txt"

    ct = base64.b64decode("".join(read_file(filename)))
    ct_blocks = split_bytestring_16(ct)
    # print(ct_blocks)

    # AES Decrypt Formula:   PT = AES_Decrypt_ECB(CT) XOR CT_Previous_Block
    pt = decrypt_CBC(ct_blocks, key, iv)
    print(pt)


if __name__ == "__main__":
    main()