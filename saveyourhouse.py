#import words from wordlist.py and import tkinter
import tkinter as tk
import random
from wordlist import word_list

#house art filler
house_art = [
"""\
    /\ 
   /  \\  
  /    \\ 
 /      \\ 
 |      |  
 | |_|  |  
"""
"""\

   /  \\  
  /    \\ 
 /      \\ 
 |      |  
 | |_|  |  
"""
"""\
   
  /    \\ 
 /      \\ 
 |      |  
 | |_|  |  
"""
"""\
    
 /      \\ 
 |      |  
 | |_|  |  
"""
"""\
   
 |      |  
 | |_|  |  
"""
"""\
   
       |  
  |_|  |  
"""
"""\
   
         
  |_|    
"""
]

def choose_word():
    return random.choice(word_list)

def update_house(tries):
    house_label.config(text=house_art[tries])

def check_guess(guess):
    global display_word
    if guess in word:
        for i in range(len(word)):
                if word[i] == guess:
                     display_word = display_word[:i] + guess + display_word[i+1:]
                     word_label.config(text=display_word)
        if "_" not in display_word:
            end_game("Lose")
    else:
        global tries
        tries += 1
        update_house(tries)
        if tries == 6:
            end_game("Lose")

def end_game(result):
    if result == "Win!":
        result_text = "You win!"
    else:
        result_text = "You lose!"
        guess_entry.config(state="disabled")
        guess_button.config(state="disabled")
        status_label.config(text=result_text)

#pop-up window
root = tk.Tk()
root.title("Save Your House")

#GUI components:

#displays the house picture
house_label = tk.Label(root,font=("Times New Roman", 12))
house_label.grid(row=0, column=0)

#displays blanks
word = choose_word()
display_word = "_"* len(word)
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

#player can request a hint
#hint_request = tk.Label(root,text="")
#hint_request.pack()

#hint category is displayed
#hint = tk.Label(root,text="")
#hint.pack()


root.mainloop()