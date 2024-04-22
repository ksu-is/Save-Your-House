#import words from wordlist.py 
import random
from wordlist import word_list

def pick_word():
    word =random.choice(word_list)
    return word.upper()

def game(word):
    word_complete = "_" * len(word)
    guessed= False 
    guessed_letters = []
    guessed_words = []
    tries = 7
    print(" Hurry! Play to Save Your House!")
    print(display_house(tries))
    print(word_complete)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_house(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_house(tries):
    stages = [  #roof sliding off, top two only
                """
      /\
    /    \
  /        \
  |        | 
  |  |__|  |
                """,
                # second tier slides off, next two
                """
      /\
    /    \
  /        \
  |        | 
  |  |__|  |
                """,
                # third tier
                """
      /\
    /    \
  /        \
  |        | 
  |  |__|  |
                """,
                # top of left wall falls, only one character missing
                """
      /\
    /    \
  /        \
  |        | 
  |  |__|  |
                """,
                # top of right wall falls, only one character missing
                """
      /\
    /    \
  /        \
  |        | 
  |  |__|  |
                """,
                # bottom of left wall falls
                """
      /\
    /    \
  /        \
  |        | 
  |  |__|  |
                """,
                # bottom of right wall falls
                """
      /\
    /    \
  /        \
  |        | 
  |  |__|  |
                """
    ]
    return stages[tries]


    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)



