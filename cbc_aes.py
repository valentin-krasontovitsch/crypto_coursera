### NOTES NOTES NOTES
### need random number generator to create 16 byte IV
### message to be encoded: get it from a file whose location is given as option to script
### for now, get msg from local string...
### maybe we don't really need functions for decrypting and encrypting...


### include AES, Random from crypto lib

from Crypto.Cipher import AES 
from Crypto import Random
from struct import *

def encrypt_aes(key,plain):
  obj=AES.new(key, AES.MODE_ECB)
  return obj.encrypt(plain)

def decrypt_aes(key,ciph):
  obj=AES.new(key, AES.MODE_ECB)
  return obj.decrypt(ciph)

def pad(string,block_size):
  i = block_size - len(string)%block_size
  string += bytes(chr(i),"ascii")*i
  #print("string = ",string)
  return string

def unpad(msg):
  return msg[:-1*int.from_bytes(msg[-1:], byteorder='big')]


### get key

key1 = b"140b41b22a29beb4061bda66b6747e14"

### get plain text msg

msg = b"Hi there, how you doing? I'm fine, thank you, how are you? Super"

### pad the message

msg = pad(msg,AES.block_size)

### empty cipher string

cipher = b""

### get IV by random

iv = Random.new().read(AES.block_size)

### prepend IV to cipher

cipher += iv



#for j in range(0,len(msg),

