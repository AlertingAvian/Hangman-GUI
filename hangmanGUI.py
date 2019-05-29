"""
Copyright (C) 2019 Patrick Maloney

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from tkinter import *
from tkinter import messagebox


''' Define Variables '''
secret = ""
secret_low = ""
secret_lst = []
hidden_secret = ""
hidden_secret_lst = []
guess = ""
tries = 6
tries_left_var = "You have " + str(tries) + " tries left."
prev_guessed = []

''' Defing Funcions '''
def new_game():
    global secret, secret_lst, hidden_secret, secret_low, hidden_secret_lst, tries, guess, tries_left_var
    guess_entry['state'] = 'disabled'
    guess_submit_btn['state'] = 'disabled'
    messagebox.showinfo("Hangman Instructions","First, enter the secret phrase in the first box. Then, have a second person enter their guess in the second box.")
    secret_entry['state'] = 'normal'
    sec_submit_btn['state'] = 'normal'
    secret = ""
    secret_low = ""
    secret_lst = []
    hidden_secret = ""
    hidden_secret_lst = []
    guess = ""
    tries =   6
    tries_left_var = "You have " + str(tries) + " tries left."
    tries_left_lbvar.set(tries_left_var)

def add_secret():
    global secret, secret_lst, hidden_secret, secret_low, hidden_secret_lst, tries
    secret = ""
    secret_low = ""
    secret_lst = []
    hidden_secret = ""
    hidden_secret_lst = []
    secret = secret_entry.get()
    if len(secret) < 1  or secret.isspace():
        messagebox.showwarning("Phrase Entry","Make sure you added something in the phrase box.")
        secret_entry.delete(0, "end")
    elif len(secret) >= 1:
        secret_low = secret.lower()
        secret_lst = [x for x in secret_low]
        print(secret_lst)
        for char in secret:
            if char != " ":
                hidden_secret_lst.append("-")
                hidden_secret += "-"
            else:
                hidden_secret_lst.append(" ")
                hidden_secret += " "
        print(hidden_secret,hidden_secret_lst)
        print(secret, secret_low)
        secret_entry.delete(0, "end")
        secret_entry['state'] = 'disabled'
        sec_submit_btn['state'] = 'disabled'
        messagebox.showinfo("Start Guessing","Now give the controls to Player 2. Player 2 when you are ready to start guessing press 'Ok'")
        guess_entry['state'] = 'normal'
        guess_submit_btn['state'] = 'normal'
        hint_var = "Hint: " + hidden_secret
        hidden_secret_lbvar.set(hint_var)
        

def submit_guess():
    global secret, secret_lst, hidden_secret, secret_low, hidden_secret_lst, guess, tries, tries_left_var
    guess = guess_entry.get()
    if guess.isspace():
        messagebox.showwarning("Guess Entry","You can't guess spaces.")
    guess_low = guess.lower()
    if guess_low == secret_low:
        print('Game Won: {0}'.format(secret))
        messagebox.showinfo("Hangman Game","You won! The phrase was " + secret)
    if guess_low not in secret_low:
        if tries == 1:
            messagebox.showinfo("Hangman Game", "You lost. The phrase was " + secret)
            guess_entry.delete(0, "end")
            tries -= 1
            new_game()
        else:
            tries -= 1
        tries_left_var = "You have " + str(tries) + " tries left."
        tries_left_lbvar.set(tries_left_var)
        print(guess + ' is not in the secret')
    print(guess)
    if guess_low in secret_lst:
        print(guess + ' is in the secret')
    guess_entry.delete(0, "end")
    # TODO: do more things
    

def exit_app():
    exit_yn = messagebox.askyesno("Hangman","Would you like to exit?")
    if exit_yn:
        root.quit()

root = Tk()
root.geometry("350x130+300+300")
root.resizable(width=False,height=False)

''' Variable Setup '''
prev_guessed_lbvar = StringVar()
hidden_secret_lbvar = StringVar()
tries_left_lbvar = StringVar()

''' Menu Toolbar '''
# ----- Main Menu -----
main_menu = Menu(root)

# ----- Game Menu -----
game_menu = Menu(main_menu, tearoff=0)
game_menu.add_command(label="New Game", command=new_game)
game_menu.add_separator()
game_menu.add_command(label="Exit", command=exit_app)

main_menu.add_cascade(label="Game",menu=game_menu)

# ----- Help Menu -----
help_menu = Menu(main_menu, tearoff=0)
# TODO: add in funcions for "About" and "Help"
help_menu.add_command(label="About")
help_menu.add_command(label="Help")

main_menu.add_cascade(label="Help",menu=help_menu)

''' Game Widgets '''
# ----- Secret Entry GUI -----
Label(root,text="Enter Phrase:").grid(row=0,column=0,sticky=E)
secret_entry = Entry(root)
sec_submit_btn = Button(root, text="Submit Phrase",command=add_secret)
secret_entry['state'] = 'disabled'
sec_submit_btn['state'] = 'disabled'
secret_entry.grid(row=0,column=1,sticky=W,ipadx=30,ipady=5)
sec_submit_btn.grid(row=0,column=2,sticky=W)

# ----- Player Info GUI -----
prev_guessed_lbl = Label(root,textvar=prev_guessed_lbvar,fg="black")
hidden_secret_lbl = Label(root,textvar=hidden_secret_lbvar)
tries_left_lbl = Label(root,textvar=tries_left_lbvar)
prev_guessed_lbl.grid(row=1,column=0,columnspan=2)
hidden_secret_lbl.grid(row=2,column=0,columnspan=2)
tries_left_lbl.grid(row=3,column=0,columnspan=2)

# ----- Player Guess Entry GUI -----
Label(root,text="Enter Guess:").grid(row=4,column=0,sticky=E)
guess_entry = Entry(root)
guess_submit_btn = Button(root,text="Submit Guess",command=submit_guess)
guess_entry['state'] = 'disabled'
guess_submit_btn['state'] = 'disabled'
guess_entry.grid(row=4,column=1,sticky=W,ipadx=30,ipady=5)
guess_submit_btn.grid(row=4,column=2,sticky=W)

''' Config and start app '''
root.title("Hangman")
root.config(menu=main_menu)
root.iconbitmap(r'C:\Users\maloneypatrick08\Documents\GitHub\Hangman-GUI\hangman_icon.ico')
root.mainloop()
