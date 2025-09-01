def multiplicative_cipher(plaintext, key):
    ciphertext = ""
    for char in plaintext.replace(" ", ""):
        mapped_number = ord(char.lower()) - ord('a')
        cipher_num = (mapped_number * key) % 26
        ciphertext += chr(ord('A') + cipher_num)
    return ciphertext

def multiplicative_decipher(ciphertext, key):
    deciphertext = ""
    def modinv(a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        raise ValueError("No modular inverse for this key.")
    inv_key = modinv(key, 26)
    for char in ciphertext:
        mapped_number = ord(char.lower()) - ord('a')
        plain_num = (mapped_number * inv_key) % 26
        deciphertext += chr(ord('A') + plain_num)
    return deciphertext

print(multiplicative_cipher("hello world", 5))
print(multiplicative_decipher("JUDDSGSHDP", 5))
