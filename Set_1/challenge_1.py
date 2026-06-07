import codecs

def xor_strings(s1, s2): 
    return "".join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(s1, s2))

def hex_to_base64(hex):
    return codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()

def main(): 
    hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    b64 = hex_to_base64(hex)
    print(b64)
    
if __name__ == "__main__":
    main()