def cipher(plaintext, key):
    char = plaintext
    mapped_number = ord(char)-ord('a')
    # print(mapped_number)
    result =  (mapped_number + key) % 26
    # print (result)
    return result

def decipher(ciphertext, key):
    char = ciphertext
    mapped_number = ord(char)-ord('a')
    # print("mapped: ",mapped_number)
    result =  (mapped_number - key) % 26
    # print (result)
    return result

key = int(input("Enter the Key: "))
text = input("Enter Text to cipher")
text = text.replace(" ","")


ciphertext = []
deciphertext = []

for w in text:
    ciphertext.append(cipher(w, key))

cipher_string = ""
for w in ciphertext:    
    cipher_string += chr(ord('A') + w )

print(cipher_string)
cipher_string = cipher_string.lower()

decipher_string = ""
for w in cipher_string:
    deciphertext.append(decipher(w, key))

for w in deciphertext:    
    decipher_string += chr(ord('A') + w )

print(decipher_string)
