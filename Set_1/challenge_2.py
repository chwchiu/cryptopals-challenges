def xor_strings(s1, s2): 
    return bytes((b1 ^ b2) for b1, b2 in zip(s1, s2))

def hex_decode_to_byte(hex):
    return bytes.fromhex(hex)

def main(): 
    hex_1 = "1c0111001f010100061a024b53535009181c"
    byte_str_1 = hex_decode_to_byte(hex_1)

    hex_2 = "686974207468652062756c6c277320657965"
    byte_str_2 = hex_decode_to_byte(hex_2)

    res = xor_strings(byte_str_1, byte_str_2)
    answer = hex_decode_to_byte("746865206b696420646f6e277420706c6179")

    assert res == answer, "Incorrect Answer"

    print("Success!")
    
if __name__ == "__main__":
    main()