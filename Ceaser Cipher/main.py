# allows for a shift past z
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    # shifting the opposite direction
    if cipher_direction == "decode":
        shift_amount *= -1
    # loops through each character
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    # prints the coded message
    print(f"Here's the {cipher_direction}d result: {end_text}")

import art
print(art.logo)

continue_y_n = False
while not continue_y_n: 
    # collects input from user
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # contines until the user says no
    continue_y_n2 = input("Do you want to continue? Type 'yes' or 'no': ")
    if continue_y_n2 == "no":
        continue_y_n = True
        print("bye")
        exit() 