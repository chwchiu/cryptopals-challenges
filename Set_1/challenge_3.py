from challenge_2 import hex_decode_to_byte

def xor_string_by_byte(s, k): 
    return bytes(b ^ k for b in s)

def get_letter_frequency(letter):
    # the space character is important, considering the text could be a sentence.
    # we also penalize all the characters that do not appear in the letter frequencies
    # have included some common punctuation
    letter_frequencies = {
        ' ': 0.080,
        'a': 0.082,
        'b': 0.015,
        'c': 0.028,
        'd': 0.043,
        'e': 0.127,
        'f': 0.022,
        'g': 0.020,
        'h': 0.061,
        'i': 0.070,
        'j': 0.0016,
        'k': 0.0077,
        'l': 0.040,
        'm': 0.024,
        'n': 0.067,
        'o': 0.075,
        'p': 0.019,
        'q': 0.012,
        'r': 0.060,
        's': 0.063,
        't': 0.091,
        'u': 0.028,
        'v': 0.0098,
        'w': 0.024,
        'x': 0.0015,
        'y': 0.020,
        'z': 0.00074,
    }

    return letter_frequencies.get(letter.lower(), -0.01)

def score_res(res):
    score = 0
    for b in res:
        score += get_letter_frequency(chr(b))

    return score

def get_most_probable_plaintext_and_key(cipher_text):
    cur_highest_score = 0
    cur_key = 0

    for key in range(256):
        res = xor_string_by_byte(cipher_text, key)
        score = score_res(res)

        if score > cur_highest_score: 
            cur_highest_score = score
            cur_key = key

    return cur_key

def main(): 
    cipher_text = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    byte_str = hex_decode_to_byte(cipher_text)

    ans_key = get_most_probable_plaintext_and_key(byte_str)

    print(ans_key)

    ans_plaintext = xor_string_by_byte(byte_str, ans_key)

    print(bytes(ans_plaintext).decode('utf-8'))
    
if __name__ == "__main__":
    main()