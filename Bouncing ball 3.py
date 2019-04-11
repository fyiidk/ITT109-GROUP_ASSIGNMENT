

from tkinter import filedialog
from tkinter import *

def mainscreen ():
    while bounce_amount < game:
        lblimage.config(pady=20)
        lblimage.config(pady=0)

game = Tk()
game.title ("Bouncing Ball")
game.minsize(500,500)
game.resizable (False, False)
mainscreen = "white"
bounce_amount = Entry().grid(row=5)
lblimage= PhotoImage(file="Basketball.png")
Label (game, text= "Welcome to Bouncing Ball", fg= "black",
       font= "none 30 bold"). grid(row=1, column=0, sticky=S)
Label (game, image = lblimage ).grid (row=10, column= 0, sticky=S)
Button(game, text="Let's Bounce!" , width= 10, command= mainscreen). grid(row=7,
        column=0, columnspan= 2, padx=15, pady=60, sticky=S)
Button(game, text="Close" , width= 10, command= game.destroy). grid(row=12,
        column=0, columnspan= 2, padx=15, pady=60, sticky=S)

