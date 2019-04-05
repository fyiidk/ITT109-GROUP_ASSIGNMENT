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




