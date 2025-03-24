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
        if charecter.isalpha(): # cheking if the charecter are all alphebetical
            shift_value = 65 if charecter.isupper() else 97  # same as line 10 and ll
            # NOT THIS AGAIN
            # Revers the shift (reversal red)
            # ORD gets the ASCII values 
            # Subtract shift value to normilize it A to 0 a to 0
            # Subtract the shift value to return them to original place in alphabet
            # the % 26 makes sure we loop around 
            # add back shit to turn it back into charecters
            decrypted_text += chr((ord(charecter) - shift_value - shift) % 26 + shift_value)
        else:
            decrypted_text += charecter  # Non-alphabet characters remain unchanged
    return decrypted_text # returns the decrypted message


def play_again(): # function to play again
    # user gets to choose id they wanna play again or not
    play = input("Would you like to use this chypher machine again [Y] or [N] ").capitalize()
    # if play again is not equal to y then
    if play != "Y":
    # calls the bye function
        bye()
    # else if play is equal to y then
    elif play == "Y":
    # call the main functin
        main()
    # other wise call the bye function
    else:
        bye()
    

def bye(): # a function to say goodbye
    print("Have a nice day") # prints a message
    exit() # exits the program

# Main Body

def main():
    # a simple statement to let the user know what the program is about
    print("Hello User, this is a simple Enigma Machine for the Caeser Cypher")
    # asks the user there name
    person = input("Whats your name user? ").capitalize

    # user gets to choose if they would like to encrypt or decrypt the message
    do_something = input(f"Hello {person}, would you like to [E]ncrypt or [D]ecrypt a message? " ).capitalize()
    # shift value input so the cypher works
    shift = int(input("Enter the shift value (1-25): "))
    # the message that the user wants to do
    message = input("whats your message? ")
     # checks if the user entered E or e so it calls the encrypt message function
    if do_something == "E":
        output = encrypt_message(message, shift)
        print(f"Encrypted Message: {output}")
        # checks if the user put and D or d and calls the decrypt message function
    elif do_something =="D":
        output = decrypt_message(message, shift)
        print(f"Decrypted Message: {output}")

    play_again()
       
        

    

   


if __name__ == "__main__":
    main()