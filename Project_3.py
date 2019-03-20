from tkinter import * 
from random import randint
from tkinter import filedialog
rules = "Here are the rules:\nRock beats Scissors\nScissors beats Paper\nand Paper beat Rock"
main_window = Tk()
main_window.title("Rock Paper Scissor: The Game")

main_menu = Menu(main_window)
sub_menu = Menu(main_menu)
main_menu.add_cascade(label="Option", menu=sub_menu)
main_window.config(menu=main_menu)
sub_menu.add_command(label="Exit", command=main_window.quit)

rules_label = Label(main_window, justify="center", fg="#000FFF", bg="#FFFFFF", text=rules)
rules_label.grid(row=0, column=0)
main_window.mainloop()