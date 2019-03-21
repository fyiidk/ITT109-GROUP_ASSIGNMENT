#! /usr/bin/python
from tkinter import * 
from random import randint
#list of possible actions
actions = ["Scissors","Rock","Paper"]
win_loss_counter = 0

#main function for determaining wins, loses and draws.
def play(label, action_list, player_choice):
	human_choice = player_choice.get()
	computer_random_int = randint(0,2)
	computer_choice = action_list[computer_random_int]
	print(str(human_choice))
	if human_choice == "Scissors" and computer_choice == "Rock":
		label.config(text="You LOSE!!!")
		win_loss_counter -= 1
	#print(computer_choice). Uncomment if you want to test if function play() is working correctly.

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
#player and computer opponent variables.
player_choice = StringVar()
outcome = Label(sideframe, pady=10,)
computer_choice = StringVar()
#creates radio buttons that player will interact with.
Radiobutton(mainframe, activebackground="#010101",pady=10, text ='Rock', variable = player_choice, value = actions[1]).grid(column=1, row=2, sticky=W)
Radiobutton(mainframe,activebackground="#010101", pady=10 ,text ='Paper', variable = player_choice, value = actions[2]).grid(column=1, row=3, sticky=W)
Radiobutton(mainframe,activebackground="#010101", pady= 10,text ='Scissors', variable = player_choice, value = actions[0]).grid(column=1, row=4, sticky=W)
Button(mainframe, text= "Submit", command=play(outcome,actions,player_choice)).grid(column=1,row=5,sticky=W)
#Keeps window from closing, DO NOT REMOVE. 
window.mainloop()