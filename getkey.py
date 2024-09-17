import binascii

def get_key(cipher_1,guessWord):
    bytes_res_1 = binascii.unhexlify(cipher_1)
    message = ""
    xorArr = []
    guess_arr = [ord(c) for c in guessWord]
    for c,k in zip(bytes_res_1,guess_arr):
        xor = c^k
        message+=chr(xor)
        xorArr.append(xor)
    print(xorArr)
    # print(message)
    return message

def read_from_file(fname):
    messages = []
    with open(fname, "r") as file:
        for line in file:
            messages.append(line.strip())
    return messages
def main():

    enc_file = "OG_streamciphertexts.txt"
    ciphers = read_from_file(enc_file)
    inp=int(input("Enter the index of the cipher "))
    first = ciphers[inp]
    e_words = "if "
    message = get_key(first,e_words)
if __name__ == "__main__":
    main()
