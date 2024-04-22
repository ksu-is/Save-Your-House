
#import words from wordlist.py and import tkinter
import tkinter as tk
import random
from wordlist import word_list

#main app window 
root = tk.Tk()
root.title("Save Your House")

#Gui components

#displays the house picture
house_label = tk.Label(root,text="")
house_label.pack()

#displays blanks
word.label=tk.Label(root, text= "")
word_label.pack()

# displays player input
guess_entry = tk.Entry(root)
guess_entry.pack()

#for players to guess a letter
guess_button= tk. Button(root,text="Guess", command=make_guess)
guess_button.pack()

#displays game status
status_label = tk.Label(root,text="")
status_label.pack()

#displays tries remaining
tries_remain = tk.Label(root,text="")
tries_remain.pack()

#player can request a hint
hint_request = tk.Label(root,text="")
hint_request.pack()

#hint category is displayed
hint = tk.Label(root,text="")
hint.pack()

def get_word():
    word =random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Hurry! You need to guess the word to save your house!")
    print(display_house(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter : ")
        guess = guess.upper()
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
            guess = guess.upper()
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
    stages = [  # final house
                """
    
       
          
           
     
                """,
                # right wall gone
                """
    
  
           
    |__|  
                """,
                # left wall gone
                """

          | 
    |__|  |
                """,
                # third tier gone
                """

  |        | 
  |  |__|  |
                """,
                # second tier gone
                """
      
    
  /        \
  |        | 
  |  |__|  |
                """,
                # roof/first tier gone
                """
     
    /    \
  /        \
  |        | 
  |  |__|  |
                """,
                # full house
                """
      /\
    /    \
  /        \
  |        | 
  |  |__|  |
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()

#comment