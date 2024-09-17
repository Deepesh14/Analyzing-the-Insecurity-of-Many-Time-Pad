
"""
PLEASE DO 'pip install pyenchant' TO INSTALL ENCAHNAT, OUR WE WILL GET ERROR
Only Compatible to run on ubuntu or debaian based system as i am using dictionary from the linux 
"""

import binascii
import enchant
DICT = enchant.Dict("en_US")

def getwords(cipher_1,cipher_2,guessWordArr):

    # XOR of two cipher text
    bytes_res_1 = binascii.unhexlify(cipher_1)
    bytes_res_2 = binascii.unhexlify(cipher_2)
    message = ""
    xorArr = []
    for c,k in zip(bytes_res_1,bytes_res_2):
        xor = c^k
        xorArr.append(xor)
        if(c == 32):
            message+="*"
        if(k == 32):
            message+="*"
        else:
            if(xor >32 and xor <=126):
                message+=chr(xor)
            else:
                message+="*"
    # print(xorArr)

    # guess the word

    guess_arr = []
    mayBeArr=[]
    for guessWord in guessWordArr:
        guess_arr = [ord(c) for c in guessWord]
        glen = len(guess_arr)
        loopLen = len(xorArr) - glen + 1
        allGuessArr=[]
        mayBeArr.append(guessWord)
        show = 0
        for i in range(loopLen):
            res_xor =""
            for ci,gi in zip(guess_arr,xorArr[i:i+glen]):
                res_xor +=chr(ci^gi)
            if(res_xor.strip().isalpha()):
                if(DICT.check(res_xor.strip())):
                    data_msg = "_"*len(xorArr)
                    try:
                        msg_xor = data_msg[:i]+res_xor+data_msg[i+glen:]

                        # need to maual change the index for which we are checking the index
                        start = 0
                        end =17
                        if(i>=start and (i+glen)<end):
                            show = 1
                            print(msg_xor,i, i+glen)
                    except Exception as e:
                        pass
                    if(len(res_xor.strip())>1):
                        allGuessArr.append(res_xor)
                        mayBeArr.append(res_xor)
        if(len(allGuessArr)!=0 and show ==1):
            print(guessWord,"===", allGuessArr)
            print()
    # print(mayBeArr)
    print(len(mayBeArr))
    return message

def read_from_file(fname):
    messages = []
    with open(fname, "r") as file:
        for line in file:
            messages.append(line.strip())
    return messages
def main():
    opt_name = "output.txt"
    enc_file = "OG_streamciphertexts.txt"
    # enc_file = "streamciphertexts.txt"
    ciphers = read_from_file(enc_file)

   # Getting dictionary 
    with open("/usr/share/dict/words") as f:
        words = f.read().splitlines()
    with open(opt_name, "wb") as opt:
        len_c = len(ciphers)
        inp =input("enter letter to start with ")
        for i in range(len_c-1):
            j = i+1
            first = ciphers[i]
            second = ciphers[j]
            print(f"XOR of {i} and {j}")
            print("-------------------------------------------------")
            get_words = [word for word in words if word.startswith(inp)]
            message = getwords(first,second,get_words)
            # message = get_msg(first,second,geg_words)
if __name__ == "__main__":
    main()
