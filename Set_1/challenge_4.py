from challenge_3 import get_letter_frequency, xor_string_by_byte, score_res
from challenge_2 import hex_decode_to_byte

def xor_strings(s1, s2): 
    return "".join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(s1, s2))

def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]

def get_most_probable_plaintext_and_score(cipher_text):
    cur_highest_score = 0
    cur_key = 0

    for key in range(256):
        res = xor_string_by_byte(cipher_text, key)
        score = score_res(res)

        if score > cur_highest_score: 
            cur_highest_score = score
            cur_key = key


    return xor_string_by_byte(cipher_text, cur_key), cur_highest_score

def find_highest_score_cipher(cipher_arr):
    score = 0
    cipher = ""
    plaintext = ""
    for cur_cipher in cipher_arr:
        byte_str = hex_decode_to_byte(cur_cipher)
        cur_plaintext, cur_highest_score = get_most_probable_plaintext_and_score(byte_str)

        if cur_highest_score >= score:
            score = cur_highest_score
            cipher = cur_cipher
            plaintext = cur_plaintext

    return score, cipher, plaintext



def main(): 
    filename = "challenge_4.txt"
    cipher_arr = read_file(filename)

    score, cipher, plaintext = find_highest_score_cipher(cipher_arr)

    print(f"Highest Score: {score}")
    print(f"Most Likely Cipher: {cipher}")
    print(f"Most Likely Plaintext: {plaintext}")
    
if __name__ == "__main__":
    main()