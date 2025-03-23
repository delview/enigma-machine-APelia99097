# Enigma Machine
# Cypher: Caeser Cipher

# Encrypt Message
def encrypt_message(plaintext, shift):
    encrypted_text = "" # an empty string to store the encrypted messgage later on
    for charecter in plaintext: # Loop through eech charecter in plaintext
        if charecter.isalpha(): # this checks if the charecters are alphabetical
            # figure out if its capital or not
            shift_value = 65 if charecter.isupper() else 97 # ASCII value for capital A is 65 and for  lower a its 97 this way we handle upper and lowercase differently
            # use 65 for capital A and 97 for lowercase 97

            # shifting the charecters (CANT WAIT TO WRITE ALL OF THIS)
            # so the ord gets the ACSII values
            # subtract the shift value to make the letter normal ex. turns A into 0 and a into 0
            # Then add the shift value givem by the user to actually cypher it, by adding we change the letter to another letter ex. is shift was 4 A would become E
            # the % 26 makes sure we can loop around the alphabet ex, after Z we go to A
            # afterwords we add back the shift value to turn them back into charecters
            # lots of bedmass and reddit disccusions were needed for this
            encrypted_text += chr((ord(charecter) - shift_value + shift) % 26 + shift_value) 
        else:
            encrypted_text += charecter # numerical values stay the same 
    return encrypted_text # returns encrypted message

# Decrypt Message
def decrypt_message(encrypted_text, shift): 
    # Empty string to store not the encrypted message later on
    decrypted_text = ""
    for charecter in encrypted_text: # loop through each charecter in encrypted text
        if charecter.isalpha(): # cheking if the charecter are all 
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