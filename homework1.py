#Author
#Neptun_Code: KEOHH7

from cryptography.fernet import Fernet                                #I am using Fernet for the generation of a Symetric Key
from Crypto.PublicKey import RSA                                      #I am using RSA for the generation of Public and Private Keys

#Beginning of Defined Fucntions:

def encryptmessage(message, key):                                     #This function allows the message to be encrypted by the Symemtric Key
    cipher=Fernet(key)                                                #Uses the Fernet module to generate the object from the key
    encoded_message= message.encode()                                 #Fernet takes bytes as input so we need to convert the string into bytes
    encrypted_message = cipher.encrypt(encoded_message)               #Encrypts the bytes using the symmetric key
    return encrypted_message                                          #Returns the encrypted message



def decryptmessage(encrypted_message, key):                          #This function allows the message encrypted by the Symmetric Key to be decoded
    cipher=Fernet(key)                                               #Uses the Fernet module to generate the object from the key
    decrypted_message= cipher.decrypt(bytes(encrypted_message))      #Takes the string and converts it into bytes and passes it to the Fernet Module for Decryption using the Symmetric Key
    return decrypted_message.decode()                                #Returns the decrypted message as a string by decoding from bytes

#Beginning of main function:

RSAKey = RSA.generate(1024)                                            #Bob's RSA Public Private Key
Pubkey=RSAKey.publickey().exportKey()                                  #Bob's Public RSA Key that he shares with Alice
print("Bob has created his Public key and sends it to Alice.")

FernetKey=Fernet.generate_key()                                        #Alice Generates a Symmetric Key
AlicePubKey=RSA.importKey(Pubkey)                                      #Alice Imports Bob's Public Key
FernetKeyEncrypted=AlicePubKey.encrypt(FernetKey, 64)                  #Alice Encrypts the Symmetric Key with Bob's Public key
print("Alice has Recieved Bobs Public key, created her Symmetric Key, encrypted her Symmetrickey with Bobs Public key and sent it to him.")

FernetKeyDecrypted=RSAKey.decrypt(FernetKeyEncrypted)                  #Bob Decrypts the Symmetric Key using his Provate RSA key
HelloEncrypted = encryptmessage('Hello', FernetKeyDecrypted)           #Bob Uses his Symmetric Key to encrypt the message Hello
print("Bob Decrypted the Symmetric Key with his Private key and was able to send an encrypted message.")

HelloDecrypted = decryptmessage(HelloEncrypted, FernetKey)             #Alice Decrypts the message using the symmetric key
print(HelloDecrypted)                                                  #Alice prints the decrypted message to read it
print("Alice could read the message encrypted by the symmetric key")
