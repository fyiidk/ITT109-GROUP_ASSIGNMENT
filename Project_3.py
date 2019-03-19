'''
from tikinter import *
from tkinter import filedialog
rules = "Here are the rules:\n*Rock beats Scissors\n*Scissors beats Paper\n*Paper beats Rock"
main_window = Tk()
main_window.title("ROCK PAPER SCISSORS")
main_window.geometry("600x600")
rules_label = Label(main_window, text=rules)
rules_label.pack()
main_window.mainloop()
'''
from tkinter import * 
from tkinter import filedialog
rules = "Here are the rules:\nRock beats Scissors\nScissors beats Paper\nPaper beat Rock"
main_window = Tk()
main_window.title("Rock Paper Scissor: The Game")
main_window.geometry("200x200")
rules_label = Label(main_window, justify="center", fg="#000FFF", bg="#FFFFFF", text=rules)
rules_label.pack()
main_window.mainloop()