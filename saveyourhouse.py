
#import words from wordlist.py and import tkinter
import tkinter as tk
import random
from wordlist import word_list

#add house art

def choose_word():
    return random.choice(word_list)

def update_house(tries):
    house_label.config(text=house_art[tries])

#main app window 
root = tk.Tk()
root.title("Save Your House")

word = ""
word_completion = ""
guessed_letters = []
guessed_words = []
tries = 6

#Gui components

#displays the house picture
house_label = tk.Label(root,font=("Times New Roman", 12))
house_label.grid(row=0, column=0)

#displays blanks
word = choose_word()
word_label=tk.Label(root, text= "_"*len(word), font=("Times New Roman", 16))
word_label.grid(row=1, column=0)

# displays player input
guess_entry = tk.Entry(root, width=3, font=("Times New Roman", 16))
guess_entry.grid(row=2, column=0)

#for players to guess a letter
guess_button= tk.Button(root, text="Guess")
guess_button.grid(row=2, column=1)

#displays game status
status_label = tk.Label(root, font=("Times New Roman", 16))
status_label.grid(row=3, column=0)

update_house(tries)

#root.mainloop()

#player can request a hint
#hint_request = tk.Label(root,text="")
#hint_request.pack()

#hint category is displayed
#hint = tk.Label(root,text="")
#hint.pack()

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

def initialize_game():
    global word, word_completion, guessed_letters, guessed_words, tries_remain
    word = get_word()
    word_completion = "_"*len(word)
    guessed_letters = []
    guessed_words = []
    tries = 6
    update_house(tries)

def make_guess():
    global word, word_completion, guesed_letters, guessed_words, tries
    guess = guess_entry.get().upper()

def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()