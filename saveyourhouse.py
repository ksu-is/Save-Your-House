#import words from wordlist.py and import tkinter
import tkinter as tk
import random
from wordlist import word_list

#house art filler
house_art = [
    "|/|\|"
]

def choose_word():
    return random.choice(word_list)

def update_house(tries):
    house_label.config(text=house_art[tries])

def play_game(guess):
    global guessed, tries, word, word_completion
    guessed = False
    tries = 0
    word = choose_word()
    word_completion = "_"* len(word)
    word_label.config(text=word_completion)

def guess_type(guess):
    if len(guess) == 1 and guess.isalpha():
        return "letter", guess.upper()
    elif len(guess) == len(word) and guess.isalpha():
        return "word", guess.upper()
    else:
        return "invalid", None
    
guessed_letters = []

def check_guess(letter_or_word, guess):

    global tries, guessed, word_completion

    if letter_or_word == "letter":
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                update_house(tries)
                tries += 1
                guessed_letters.append(guess)
            else:
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
                tries += 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
    else:
        print("Not a valid guess.")
    print(update_house(tries))
    print(word_completion)
    print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

def play_game(guess):
    global guessed, tries, word, word_completion
    guessed = False
    tries = 0
    word = choose_word()
    word_completion = "_"* len(word)
    word_label.config(text=word_completion)

def make_guess():
    guess = input("Enter your guess: ")
    guess_type, guess = check_guess(guess)
    message, game_over = check_guess(guess_type, guess)
    status_label.config(text=message)
    if game_over:
        guess_button.config(state=tk.DISABLED)

#pop-up window
root = tk.Tk()
root.title("Save Your House")

#GUI components:

#displays the house picture
house_label = tk.Label(root,font=("Times New Roman", 12))
house_label.grid(row=0, column=0)

#displays blanks
word = choose_word()
word_label=tk.Label(root, text= "_"*len(word), font=("Times New Roman", 16))
word_label.grid(row=1, column=0)

#displays player input
guess_entry = tk.Entry(root, width=3, font=("Times New Roman", 16))
guess_entry.grid(row=2, column=0)

#for players to guess a letter
guess_button= tk.Button(root, text="Guess")
guess_button.grid(row=2, column=1)

#displays game status
status_label = tk.Label(root, font=("Times New Roman", 16))
status_label.grid(row=3, column=0)

play_game()

root.mainloop()

#player can request a hint
#hint_request = tk.Label(root,text="")
#hint_request.pack()

#hint category is displayed
#hint = tk.Label(root,text="")
#hint.pack()