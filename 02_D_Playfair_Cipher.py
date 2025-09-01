def create_key_square(keyword):
 
    keyword = keyword.upper().replace(" ", "").replace("J", "I")
    
  
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
   
    key_square_chars = []
 
    for char in keyword:
        if char not in key_square_chars:
            key_square_chars.append(char)
            
   
    for char in alphabet:
        if char not in key_square_chars:
            key_square_chars.append(char)
            
    
    key_square = [key_square_chars[i:i+5] for i in range(0, 25, 5)]
    return key_square

def find_position(char, key_square):
    
    for r in range(5):
        for c in range(5):
            if key_square[r][c] == char:
                return r, c
    return -1, -1 

def prepare_plaintext(plaintext):
    
    text = plaintext.upper().replace(" ", "").replace("J", "I")
    
    prepared_text = ""
    i = 0
    while i < len(text):
        
        char1 = text[i]
        
        
        if i + 1 == len(text) or char1 == text[i+1]:
            
            prepared_text += char1 + 'X'
            i += 1 
        else:
            
            prepared_text += char1 + text[i+1]
            i += 2 
            
    return prepared_text

def playfair_cipher(text, key_square, mode):
    
    processed_text = ""
    
    
    if mode == 'encrypt':
        shift = 1
    elif mode == 'decrypt':
        shift = -1
    else:
        return "Invalid mode selected."

    
    for i in range(0, len(text), 2):
        char1 = text[i]
        char2 = text[i+1]
        
        r1, c1 = find_position(char1, key_square)
        r2, c2 = find_position(char2, key_square)
        
        
        if r1 == r2:
            processed_text += key_square[r1][(c1 + shift) % 5]
            processed_text += key_square[r2][(c2 + shift) % 5]
        
        
        elif c1 == c2:
            processed_text += key_square[(r1 + shift) % 5][c1]
            processed_text += key_square[(r2 + shift) % 5][c2]
            
       
        else:
            processed_text += key_square[r1][c2]
            processed_text += key_square[r2][c1]
            
    return processed_text


if __name__ == "__main__":
    
    keyword = "PLAYFAIR EXAMPLE"
    plaintext = "HIDE THE GOLD IN THE TREE"

    
    key_square = create_key_square(keyword)
    
    print("--- Key Square ---")
    for row in key_square:
        print(row)
    print("-" * 20)

    
    prepared_text = prepare_plaintext(plaintext)
    
    
    ciphertext = playfair_cipher(prepared_text, key_square, 'encrypt')
    
    print(f"Plaintext:      {plaintext}")
    print(f"Prepared Text:  {prepared_text}")
    print(f"Encrypted Text: {ciphertext}")
    
    
    decrypted_text = playfair_cipher(ciphertext, key_square, 'decrypt')
    
    print(f"Decrypted Text: {decrypted_text}")
