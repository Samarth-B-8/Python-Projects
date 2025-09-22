# Import necessary libraries and modules
import random
import hangman_words
import art

# Initialised the word_list from hangman module
word_list = hangman_words.word_list
lives = 6

# Import the logo from hangman_art.py
logo = art.logo_hangman
print(logo)

# Choose the word for the game
chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # The remaining lives is displayed to the user
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # Display the letter that they have guessed
    display = ""
    if guess in correct_letters:
        print(f"You have already guessed {guess}")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True

            #  Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************YOU LOSE**********************")
            print(f"It was {chosen_word}! You lost!.")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Stages of the hangman
    stages = art.stages
    print(stages[lives])

