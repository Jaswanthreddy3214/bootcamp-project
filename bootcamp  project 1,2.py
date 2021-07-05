#project 1
# python program to generate md5 of string data


import hashlib
#project1
# python program to generate md5 of string data
def md5_hashing(string):
    encode = hashlib.md5(string.encode())
    return (encode)

#project 2
#python program to generate 3 different algorithms using hashlib

def sha256_hashing(string):
    encode=hashlib.sha256(string.encode())
    return (encode)

def blake2s_hashing(string):
    encode1=hashlib.blake2s()
    encode1.update(string.encode())
    return (encode1)

def sha224_hashing(string):
    encode2=hashlib.sha224(string.encode())
    return (encode2)

string=input()
#project 1
encoded_string = md5_hashing(string)
print("the binary equivalent of md5 is :")
print(encoded_string.digest())
print("The Hexadecimal equivalent of md5 is:")
print(encoded_string.hexdigest())
print(" ")

#project 2

encoded_value=sha256_hashing(string)
print("the byte equivalent of sha256 : ")
print(encoded_value.digest())
print("The hexadecimal equivalent of sha256 :")
print(encoded_value.hexdigest())
print(" ")

encoded_value1=blake2s_hashing(string)
print("the byte equivalent of blake2s is :")
print(encoded_value1.digest())
print("the hexadecimal equivalent of blake2s is :")
print(encoded_value1.hexdigest())
print(" ")

encoded_value2=sha224_hashing(string)
print("the binary equivalent of sha224 is :")
print(encoded_value2.digest())
print("the hexadecimal equivalent of sha224 is: ")
print(encoded_value2.hexdigest())

