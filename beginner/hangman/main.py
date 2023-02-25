import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

chosen_word = random.choice(word_list)
chosen_word_list = list(chosen_word)
print(chosen_word)

# Set Guessed Word List
guessed_word_list = ["_"] * len(chosen_word_list)
LIVES = 6
END_OF_GAME = False

# Word Validation
while not END_OF_GAME:
    user_letter_guess = input(
        f"Pick a letter. You have {LIVES} lives remaining.").lower()

    if (user_letter_guess in guessed_word_list):
        print(f"You have already picked {user_letter_guess}. Try again.")
    else:
        for position in range(len(chosen_word)):
            # Check if guess in word
            if (chosen_word[position] == user_letter_guess):
                guessed_word_list[position] = user_letter_guess

        # Check solution completed
        if ("_" not in guessed_word_list):
            print("YOU WIN")
            END_OF_GAME = True

        # Removes life if incorrect guess
        if (user_letter_guess not in chosen_word):
            LIVES -= 1
            if LIVES == 0:
                print("YOU LOOOOSE")
                END_OF_GAME = True

    print(f"{' '.join(guessed_word_list)}")
    print(stages[LIVES])
