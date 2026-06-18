def pkcs7_padding(plaintext: str, blocksize: int) -> str:
    # Note that no matter what, pkcs7 will always pad, meaning 
    # that it would pad even if exact blocksize is met
    padding_required = blocksize - (len(plaintext) % blocksize)
    return plaintext + "\x04" * padding_required

def main(): 
    plaintext = "YELLOW SUBMARINE"
    print(pkcs7_padding(plaintext, 4).encode('utf-8'))

if __name__ == "__main__":
    main()