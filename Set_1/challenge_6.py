from challenge_3 import score_res
from challenge_4 import read_file
import base64

## Adjust parameters to get the key
MIN_KEY_SIZE = 2
MAX_KEY_SIZE = 40
NUM_NHD_BLOCKS = 20   # The greater the hamming distance considered, the easier it is to find the correct key
TOP_N_KEYS = 3

def compute_hamming_distance(byte_str_1, byte_str_2): 
    if len(byte_str_1) != len(byte_str_2):
        raise ValueError("The lengths of the two strings are not equal")
    
    distance = 0
    for b1, b2 in zip(byte_str_1, byte_str_2):
        distance += bin(b1 ^ b2).count('1')

    return distance

# def compute_normalized_hamming_distance(ciphertext, keysize):
#     return compute_hamming_distance(ciphertext[0:keysize], ciphertext[keysize:keysize*2]) / keysize

def compute_normalized_hamming_distance(ciphertext, keysize):
    # take up to NUM_NHD_BLOCKS blocks of length keysize
    blocks = [ciphertext[i:i+keysize] for i in range(0, keysize * NUM_NHD_BLOCKS, keysize)]
    # keep only full-size blocks
    blocks = [b for b in blocks if len(b) == keysize]
    if len(blocks) < 2:
        return compute_hamming_distance(ciphertext[0:keysize], ciphertext[keysize:keysize*2]) / keysize

    distances = []
    for i in range(len(blocks) - 1):
        distances.append(compute_hamming_distance(blocks[i], blocks[i+1]) / keysize)

    return sum(distances) / len(distances)

def transpose_blocks(ciphertext_blocks):
    transposed_blocks = []
    for i in range(len(ciphertext_blocks[0])):
        transposed_block = bytearray()
        for block in ciphertext_blocks:
            if i < len(block):
                transposed_block.append(block[i])
        transposed_blocks.append(transposed_block)
    return transposed_blocks

def get_most_probable_plaintext_and_score(cipher_text):
    cur_highest_score = 0
    cur_key = 0

    for key in range(256):
        res = xor_bytestr_by_key(cipher_text, key)
        score = score_res(res)

        if score > cur_highest_score: 
            cur_highest_score = score
            cur_key = key


    return xor_bytestr_by_key(cipher_text, cur_key), cur_highest_score, cur_key

def xor_bytestr_by_key(bstr, k): 
    return bytes([b ^ k for b in bstr])

def repeating_xor(s, key): 
    result = b''
    for i, c in enumerate(s):
        # print(c)
        # print(key[i % len(key)])
        # print(ord(c) ^ ord(key[i % len(key)]))
        result += bytes([c ^ key[i % len(key)]])

    return result

def main(): 
    filename = "challenge_6.txt"
    ciphertext = "".join(read_file(filename))
    b64_decoded_ciphertext = base64.b64decode(ciphertext)

    # 1. Assumptions KEYSIZE is between 2 - 40
    # 2. Test Hamming Distance function
    test_1 = b'this is a test'
    test_2 = b'wokka wokka!!!'

    print(compute_hamming_distance(test_1, test_2))

    assert compute_hamming_distance(test_1, test_2) == 37, "The hamming distance function has been implemented incorrectly"
    print("The hamming distance function is implemented correctly")

    # 3. Find Normalized Hamming Distance for all key sizes
    nhd_arr = []
    for i in range(MIN_KEY_SIZE, MAX_KEY_SIZE + 1):
        nhd = compute_normalized_hamming_distance(b64_decoded_ciphertext, i)
        nhd_arr.append((i, nhd))
    
    # 4. Find the smallest 2-3 Key Sizes
    sorted_nhd_arr = sorted(nhd_arr, key=lambda x:x[1])
    min_3_nhd_arr = sorted_nhd_arr[0:TOP_N_KEYS]

    keys = []
    for keysize, _ in min_3_nhd_arr: 
        # 5. Split the ciphertext into blocks of each keysize
        ciphertext_blocks = [b64_decoded_ciphertext[i:i + keysize] for i in range(0, len(b64_decoded_ciphertext), keysize)]

        # 6. Now transpose the blocks
        transposed_blocks = transpose_blocks(ciphertext_blocks)

        key = b""
        for tb in transposed_blocks:
            pt, score, key_byte = get_most_probable_plaintext_and_score(tb)
            key += bytes([key_byte])

        keys.append(key)

    # print(f"possible keys {keys}")
    # print(b64_decoded_ciphertext)

    for k in keys: 
        pt = repeating_xor(b64_decoded_ciphertext, k)
        print(f"current key: {k}")
        print(f"plaintext: {pt}")


if __name__ == "__main__":
    main()
