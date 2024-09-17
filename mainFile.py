import binascii
import json
# key = [201, 185, 116, 95, 158, 226, 145,176,149,23,140,204, 45, 231, 176, 101, 78,215,188,24,165, 176, 55, 91, 250, 88, 203]

key = [201, 185, 116, 95, 158, 226, 145,176,149,23,140,204, 45, 231, 176, 101, 78,215,188,24,228,178,49, 91, 248, 85,134, 201, 35, 112, 251, 76, 229, 99, 123, 46, 13, 86, 138,24, 104,182, 20, 140,91, 108, 195, 20,160,77,185,122,20,0,165, 8, 237, 6,34,249,24,138,187, 84, 56, 47, 199, 70, 224, 68, 166, 33,110, 77, 21, 163, 50, 65, 137,8,18, 96,134, 73, 104,0, 210, 70, 2, 225, 201, 51, 158, 3, 230, 202, 193,244, 165,107, 84, 65,171, 12, 172, 55, 117, 98, 192,56, 144, 179, 58, 133, 80, 79, 36, 20, 13,15, 21, 120, 177, 58, 50, 178, 202, 10, 209, 72, 4, 68, 139, 203, 217, 247, 19,242, 33, 35]
def get_key(cipher_1,key):
    bytes_res_1 = binascii.unhexlify(cipher_1)
    message = ""
    xorArr = []

    for c,k in zip(bytes_res_1,key):
        if(k == -1):
            message+="*"
        else:
            xor = c^k
            message+=chr(xor)
            xorArr.append(xor)
    print(message)
    return message

def read_from_file(fname):
    messages = []
    with open(fname, "r") as file:
        for line in file:
            messages.append(line.strip())
    return messages


def main():

    global key
    enc_file = "OG_streamciphertexts.txt"
    ciphers = read_from_file(enc_file)
    len_c = len(ciphers)
    keyStr=""
    msgArr=[]
    keyObj={"ascii_key":key,"hex_key":""}
    for ele in key:
       keyStr+=chr(ele)
    hex_key = binascii.hexlify(keyStr.encode()).decode()
    print(hex_key)
    for i in range(len_c):
        first = ciphers[i]
        print(f"For index {i}")
        try:
            message = get_key(first,key)
            msgArr.append(message)
        except Exception as e:
            print(e)

    with open('messages.txt', 'w', encoding='utf-8') as file:
        for msg in msgArr:
            file.write(f"{msg}\n")
    keyObj["hex_key"]=hex_key
    with open('key.txt', 'w', encoding='utf-8') as file1:
        json.dump(keyObj, file1, ensure_ascii=False, indent=4)
if __name__ == "__main__":
    main()
