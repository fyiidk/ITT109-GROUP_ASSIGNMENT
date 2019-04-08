from tkinter import filedialog
from tkinter import *

def mainscreen ():
    print ("Main Program")

game = Tk()
game.title ("Bouncing Ball")
game.minsize (500,500)

lblimage = PhotoImage(file="Basketball.png")
Label(game, text="Welcome to Bouncing Ball", bg="white", fg="black",
      font="none 20 bold"). grid(row=1, column =0, sticky=S)
Label(game, image=lblimage, bg="white").grid(row = 6, column = 1, sticky=W)

from tkinter import filedialog
from tkinter import *

def mainscreen ():
    while bounce_amount < game:
        lblimage.config(pady=20)
        lblimage.config(pady=0)

game = Tk()
game.title ("Bouncing Ball")
game.minsize(500,500)
bounce_amount = Entry().grid(row=5)
lblimage= PhotoImage(file="Basketball.png")
Label (game, text= "Welcome to Bouncing Ball", bg= "white", fg= "black",
       font= "none 30 bold"). grid(row=1, column=0, sticky=S)
Label (game, image = lblimage , bg= "white").grid (row=10, column= 0, sticky=S)
Button(game, text="Let's Bounce!" , width= 10, command= mainscreen). grid(row=7,
        column=0, columnspan= 2, padx=15, pady=60)

                                                                    





