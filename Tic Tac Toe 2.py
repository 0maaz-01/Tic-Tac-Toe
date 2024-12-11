from tkinter import *
import random

def next_turn(row, column):  #

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(player[1]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[0] +" wins"))

            elif check_winner() == "Tie":
                label.config(text=("Tie!"))

        else:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(player[0] + " turn"))

            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))

            elif check_winner() == "Tie":
                label.config(text=("Tie!"))


def check_winner(): #
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text']==buttons[row][2]['text'] !="":
            buttons[row][0].config(bg='yellow')
            buttons[row][1].config(bg='yellow')
            buttons[row][2].config(bg='yellow')
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text']==buttons[2][column]['text'] !="":
            buttons[0][column].config(bg='yellow')
            buttons[1][column].config(bg='yellow')
            buttons[2][column].config(bg='yellow')
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text']==buttons[2][2]['text'] != "": #First Diagonal
        buttons[0][0].config(bg='yellow')
        buttons[1][1].config(bg='yellow')
        buttons[2][2].config(bg='yellow')
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text']==buttons[2][0]['text'] != "": # Second Diagonal
        buttons[0][2].config(bg='yellow')
        buttons[1][1].config(bg='yellow')
        buttons[2][0].config(bg='yellow')
        return True

    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="orange")
        return "Tie"

    else:
        return False

def empty_spaces():   #
    spaces = 9
    for row in range(3):
        for column in range (3):
            if buttons[row][column]['text']!="":
                spaces-=1

    if spaces==0:
        return False
    else:
        return True

def new_game():
    global player
    player = random.choice(players)
    label.config(text= player + " turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text = "", bg= "#black")

window = Tk()
window.title("Tic Tac Toe")
window.config(background="black")
icon = PhotoImage(file = "C:\\Users\\alize\\Desktop\\Logo\\Tic Tac Toe.png")
window.iconphoto(True, icon)
players = ["x","o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text = player + "'s turn", font= ('consolas',40), background="black", foreground="#00FF00")
label.pack(side = "top")

reset_button = Button(text= "Play Again", font=('consolas',20), command=new_game, background="black", foreground="#00FF00", bd=10, relief=RIDGE )
reset_button.pack(side="top")

frame = Frame(window, background="black")
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40),width=5, height =2, background="black", foreground="#00FF00",
                                      activebackground="black", activeforeground="#00FF00", bd = 10, relief= RIDGE, command= lambda row=row,
                                      column=column: next_turn(row,column))

        buttons[row][column].grid(row=row,column=column)

window.mainloop()