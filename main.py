# Enigma Machine
# Cypher: Caeser Cipher

# Encrypt Message
def encrypt_message(plaintext, shift):
    encrypted_text = ""
    for charecter in plaintext:
        if charecter.isalpha():
            shift_value = 65 if charecter.isupper() else 97 # this took awhile to figure out 65 = A while 97 = a so upper/lower
            encrypted_text += chr((ord(charecter) - shift_value + shift) % 26 + shift_value)
        else:
            encrypted_text += charecter # numerical values stay the same
    return encrypted_text

# Decrypt Message
def decrypt_message(encrypted_text, shift):
    decrypted_text = ""
    for charecter in encrypted_text:
        if charecter.isaplpha():
            shift_value = 65 if charecter.isupper() else 97  # ASCII value for A/a
            decrypted_text += chr((ord(charecter) - shift_value - shift) % 26 + shift_value)
        else:
            decrypted_text += charecter  # Non-alphabet characters remain unchanged
    return decrypted_text
# Main Body