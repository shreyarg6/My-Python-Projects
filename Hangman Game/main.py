import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "-"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"********{lives}/6 Left!********")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You already guessed this letter: {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, which is not in the word. You lose a life!")
        
        if lives == 0:
            game_over = True
            print(f"You lost! The word was {chosen_word}")

    if "_" not in display:
        game_over = True
        print("You win.")

    print(stages[lives])