def affine_cipher(plaintext, a, b):
    ciphertext = ""
    for char in plaintext.replace(" ", ""):
        mapped_number = ord(char.lower()) - ord('a')
        cipher_num = (a * mapped_number + b) % 26
        ciphertext += chr(ord('A') + cipher_num)
    return ciphertext

def affine_decipher(ciphertext, a, b):
    deciphertext = ""
    def modinv(a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        raise ValueError("No modular inverse for this key.")
    inv_a = modinv(a, 26)
    for char in ciphertext:
        mapped_number = ord(char.lower()) - ord('a')
        plain_num = (inv_a * (mapped_number - b)) % 26
        deciphertext += chr(ord('A') + plain_num)
    return deciphertext

print(affine_cipher("hello world", 5, 8))
print(affine_decipher("RCLLAOAPLX", 5, 8))
