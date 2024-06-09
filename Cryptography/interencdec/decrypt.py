import base64


def decode_base64(encoded_string):
    # Decode the Base64 encoded string
    decoded_bytes = base64.b64decode(encoded_string)
    try:
        # Try to convert bytes to string assuming it's UTF-8
        decoded_string = decoded_bytes.decode('utf-8')
    except UnicodeDecodeError:
        # If it's not valid UTF-8, return the raw bytes
        decoded_string = decoded_bytes
    return decoded_string


def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_text = ""
    
    for char in ciphertext:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            ascii_offset = 65 if char.isupper() else 97
            # Shift the character back and wrap around the alphabet if needed
            decrypted_char = chr(((ord(char) - ascii_offset - shift) % 26) + ascii_offset)
            decrypted_text += decrypted_char
        else:
            # Non-alphabetic characters are added to the result without change
            decrypted_text += char
    
    return decrypted_text

# Example usage
ciphertext = "wpjvJAM{jhlzhy_k3jy9wa3k_890k2379}"
for shift in range(1, 26):
    decrypted_text = decrypt_caesar_cipher(ciphertext, shift)
    if decrypted_text[:4] == "pico":
        print("Decrypted text:", decrypted_text)
        break