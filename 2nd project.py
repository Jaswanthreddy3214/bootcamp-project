#python program to generate 3 different algorithms using hashlib
import hashlib

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

