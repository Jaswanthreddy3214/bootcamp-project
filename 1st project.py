#python program to generate md5 of string data

import hashlib

def md5_hashing(string):
    encode = hashlib.md5(string.encode())
    return (encode)
#input the string value
string = input()
encoded_string=md5_hashing(string)
print("The binary equivalent of md5 is:")
print(encoded_string.digest())
print("The Hexadecimal equivalent of md5 is:")
print(encoded_string.hexdigest())



