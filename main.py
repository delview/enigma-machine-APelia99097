# Enigma Machine
# Cypher: Caeser Cipher

# Encrypt Message
def encrypt_message(plaintext, shift):
    encrypted_message = ""
    for charecter in plaintext:
        if charecter.isalpha():
            shift_value = 65 if charecter.isupper() else 97 # this took awhile to figure out 65 = A while 97 = a so upper/lower
            encrypted_text += chr((ord(charecter) - shift_value + shift) % 26 + shift_value)
        else:
            encrypted_text += charecter # numerical values stay the same
    return encrypted_message

# Decrypt Message

# Main Body