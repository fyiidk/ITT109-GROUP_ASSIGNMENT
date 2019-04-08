#! /usr/bin/python
from tkinter import *
from random import randint

#main function for determaining wins, loses and draws.
def play(event):
	#Images for Choices
	scissor_image = PhotoImage(file="scissor.png")
	rock_image = PhotoImage(file="rock.png")
	paper_image = PhotoImage(file="paper.png")

	output = Label(sideframe, pady=10)
	output.grid(column=1, row=1)

	human_choice = player_choice.get()
	actions = ["Scissors","Rock","Paper"]
	computer_choice = actions[randint(0,2)]
	print(f"Computer: {computer_choice}")
	print(f"Player: {human_choice}")
	if player_choice == computer_choice:
		return "Draw"
		output.config(text="Draw")
	if player_choice == "Rock" and computer_choice == "Paper":
		return "Computer Wins"
		output.config(text="Computer wins")
	if player_choice == "Paper" and computer_choice == "Scissors":
		return "Computer Wins"
		output.config(text="Computer Wins")
	if player_choice == "Scissors" and computer_choice == "Rock":
		return "Computer Wins"
		output.config(text="Computer Wins")
	else:
		return "Player Wins"
		output.config(text="Player Wins")


#Makes a window to place things inside of :3
window = Tk()
window.title("Rock, Paper, Scissors")
window.geometry("300x300")

#creates the frame in which the player will interact with.
mainframe = Frame(window, padx=20, pady=12)
mainframe.grid(column=0, row = 0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0,weight=1)

#creates frame where output will be placed. (not finished)
sideframe = Frame(window, padx=20, pady=12)
sideframe.grid(column=1, row = 0, sticky=(N,W,E,S))
sideframe.columnconfigure(0, weight=1)
sideframe.rowconfigure(0,weight=1)

#player variable.
player_choice  = StringVar()

#creates buttons that player will interact with.
rock_radiobutton = Radiobutton(mainframe, pady=10, text ='Rock', variable = player_choice, value = "Rock")
rock_radiobutton.grid(column=1, row=2, sticky=W)

paper_radiobutton = Radiobutton(mainframe,  pady=10 ,text ='Paper', variable = player_choice, value = "Paper")
paper_radiobutton.grid(column=1, row=3, sticky=W)

scissors_radiobutton = Radiobutton(mainframe, pady= 10,text ='Scissors', variable = player_choice, value = "Scissors")
scissors_radiobutton.grid(column=1, row=4, sticky=W)

submit_button = Button(mainframe, pady=10, text="Submit", width=3, height=1)
submit_button.bind("<Button-1>", play)
submit_button.grid(column=1, row=6, sticky=W)
#Keeps window from closing, DO NOT REMOVE.
window.mainloop()
