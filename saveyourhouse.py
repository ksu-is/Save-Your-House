#import words from wordlist.py 
import random
from wordlist import word_list

def pick_word():
    word =random.choice(word_list)
    return word.upper()

def game(word):
    word_complete = "_" * len(word)
    guess= False 
    guess_letters = []
    guess_words = []
    tries = 7
    print(" Hurry! Play to Save Your House!")
    print(display_house(tries))
    print(word_complete)
    print("\n")
    while not guess and 
     


      /\
    /    \
  /        \
  |        | 
  |  |__|  |
>>>>>>> Stashed changes
