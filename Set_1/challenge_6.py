def string_to_binary(str): 
    return ''.join(format(ord(c), '08b') for c in str)

def binary_to_string(str):
    return ''.join(format(b, '08b') for b in bytearray(str, 'utf-8'))

def compute_hamming_distance(str_1, str_2): 
    distance = 0
    bin_1 = string_to_binary(str_1)
    bin_2 = string_to_binary(str_2)

    if len(bin_1) != len(bin_2):
        raise ValueError("The lengths of the two strings are not equal")
    
    for i, c in enumerate(bin_1):
        print(bin_1[i])
        print(bin_2[i])
        distance += ord(bin_1[i]) ^ ord(bin_2[i])

    return distance
        

def main(): 
    # 1. Assumptions KEYSIZE is between 2 - 40
    # 2. Test Hamming Distance function
    test_1 = "this is a test"
    test_2 = "wokka wokka!!!"

    assert compute_hamming_distance(test_1, test_2) == 37, "The hamming distance function has been implemented incorrectly"
    print("The hamming distance function is implemented correctly")

    

if __name__ == "__main__":
    main()
