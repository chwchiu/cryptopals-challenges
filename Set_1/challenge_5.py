def repeating_xor(s, key): 
    result = b''
    for i, c in enumerate(s):
        # print(c)
        # print(key[i % len(key)])
        # print(ord(c) ^ ord(key[i % len(key)]))
        result += bytes([ord(c) ^ ord(key[i % len(key)])])

    return result

def bytes_to_hex(bytes):
    return bytes.hex()


def main(): 
    string_1 = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""

    key ="ICE"

    print(bytes_to_hex(repeating_xor(string_1, key)))

    answer = """0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"""
    
if __name__ == "__main__":
    main()
