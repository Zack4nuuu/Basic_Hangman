# hangman.py 
#Here is where a word is selected from the words.txt file and chosen at random to be used in the game.
import string
from random import choice

def select_word():
    with open("Words.txt.txt", mode="r") as words:
        word_list = words.readlines()
    return choice(word_list).strip()

# Here is were the players input is gathered and validated.
def get_player_input(guessed_letters):
    while True:
        player_input = input("Guess a letter: ").lower()
        if validate_input(player_input, guessed_letters):
            return player_input

# this function performs three checks to make sure only one character in entered, the input is a lowercase letter between a and z, aswell as the letter has not been guessed previously.    
def validate_input(player_input, guessed_letters):
    return(
        len(player_input) == 1
        and player_input in string.ascii_lowercase
        and player_input not in guessed_letters
    )
# Here is where the guessed letters are tracked and sorted.
def join_guessed_letters(guessed_letters):
    return " ".join(sorted(guessed_letters))

# This is the function used to buld the word and show it to the player.
def build_guessed_word(target_word, guessed_letters):
    current_letters = []
    for letter in target_word:
        if letter in guessed_letters:
            current_letters.append(letter)
        else:
            current_letters.append("_")
    return " ".join(current_letters)

# Different states of the hangman when incorrect guesses occur.
def draw_hanged_man(wrong_guesses):
    hanged_man = [
        r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
    ]

    print(hanged_man[wrong_guesses])
# Amount of guesses the player gets before game over.
MAX_INCORRECT_GUESSES = 6

# Game over function
def game_over(wrong_guesses, target_word, guessed_letter):
    if wrong_guesses == MAX_INCORRECT_GUESSES:
        return True
    if set(target_word) <= guessed_letters:
        return True
    return False

if __name__ == "__main__":
    # This is the Initail setup of the game
    target_word = select_word()
    guessed_letters = set()
    guessed_word = build_guessed_word(target_word, guessed_letters)
    wrong_guesses = 0
    print("Welcome to Zacks Hangman!")

# This is where the game loop begins
if __name__ == "__main__":
    while not game_over(wrong_guesses, target_word, guessed_letters):
        draw_hanged_man(wrong_guesses)
        print(f"Your word is: {guessed_word}")
        print(
            "Current guessed letters: "
            f"{join_guessed_letters(guessed_letters)}\n"
        )

        player_guess = get_player_input(guessed_letters)
        if player_guess in target_word:
            print("Greate guess!")
        else:
            print("Sorry! That letter isnt there")
            wrong_guesses += 1

        guessed_letters.add(player_guess)
        guessed_word = build_guessed_word(target_word, guessed_letters)

# This is then game over part of the loop
if __name__ == "__main__":
    draw_hanged_man(wrong_guesses)
    if wrong_guesses == MAX_INCORRECT_GUESSES:
        print("Sorry, you lose!")
    else:
        print("Congrats! You did it!")
    print(f"Your word was: {target_word}")
