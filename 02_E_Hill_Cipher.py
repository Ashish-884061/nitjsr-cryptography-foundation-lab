import numpy as np

def hill_cipher_encrypt(plaintext, key_matrix):
    plaintext = plaintext.replace(" ", "").lower()
    n = key_matrix.shape[0]
    # Pad plaintext if necessary
    while len(plaintext) % n != 0:
        plaintext += 'x'
    ciphertext = ''
    for i in range(0, len(plaintext), n):
        block = [ord(char) - ord('a') for char in plaintext[i:i+n]]
        block_vec = np.array(block).reshape((n, 1))
        cipher_vec = np.dot(key_matrix, block_vec) % 26
        for num in cipher_vec:
            ciphertext += chr(int(num) + ord('A'))
    return ciphertext

def modinv_matrix(matrix, modulus):
    det = int(round(np.linalg.det(matrix)))
    det_inv = pow(det % modulus, -1, modulus)
    matrix_modinv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )
    return matrix_modinv

def hill_cipher_decrypt(ciphertext, key_matrix):
    n = key_matrix.shape[0]
    key_inv = modinv_matrix(key_matrix, 26)
    plaintext = ''
    for i in range(0, len(ciphertext), n):
        block = [ord(char) - ord('A') for char in ciphertext[i:i+n]]
        block_vec = np.array(block).reshape((n, 1))
        plain_vec = np.dot(key_inv, block_vec) % 26
        for num in plain_vec:
            plaintext += chr(int(num) + ord('a'))
    return plaintext


key = np.array([[3, 3], [2, 5]])
encrypted = hill_cipher_encrypt("help", key)
print(encrypted)
decrypted = hill_cipher_decrypt(encrypted, key)
print(decrypted)
