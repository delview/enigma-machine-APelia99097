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
        if charecter.isalpha():
            shift_value = 65 if charecter.isupper() else 97  # ASCII value for A/a
            decrypted_text += chr((ord(charecter) - shift_value - shift) % 26 + shift_value)
        else:
            decrypted_text += charecter  # Non-alphabet characters remain unchanged
    return decrypted_text
# Main Body

def main():
    print("Hello User, this is a simple Enigma Machine for the Caeser Cypher")

    do_something = input("Would you like to [E]ncrypt or [D]ecrypt a message? " ).capitalize()

    shift = int(input("Enter the shift value (1-25): "))

    message = input("whats your message? ")

    if do_something == "E":
        output = encrypt_message(message, shift)
        print(f"Encrypted Message: {output}")

    elif do_something =="D":
        output = decrypt_message(message, shift)
        print(f"Decrypted Message: {output}")


if __name__ == "__main__":
    main()