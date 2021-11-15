import random, time
from tkinter import *

root = Tk()
root.title = 'Rock/paper/scissors'
root.config(padx=100,pady=100)

scr = Label(root, text='Welcome to the game!')

possible = ["rock","paper","scissors"]

log = {}

def choose(input):
    global scr,choice
    choice = input
    scr.config(text=f'Your choice is: {choice}')
    

def pc_choose():
    global pc_choice
    scr.config(text='Computer is choosing...')
    rock.config(state=DISABLED)
    paper.config(state=DISABLED)
    scissors.config(state=DISABLED)
    pc_choice = "".join(random.choices(possible, k=1))
    print(pc_choice)
    try: compare()
    except NameError:
        scr.config(text='Please choose an option')
        time.sleep(1)
        reset()

def compare():
    global scr
    if pc_choice == choice:
        text = "Tied!"
    elif possible.index(pc_choice) > possible.index(choice):
        text = "You lose!"
    elif pc_choice == "rock" and choice == 'scissors':
        text = "You lose!"
    else:
        text = "You win!"
    now = time.strftime("%d/%m/%Y %H:%M:%S")
    scr.config(text=text)
    send.config(text='Again', command=reset)
    log.setdefault(now,[choice,pc_choice,text])

def reset():
    send.config(text='Start',command=pc_choose)
    scr.config(text='Choose a button')
    rock.config(state=NORMAL)
    paper.config(state=NORMAL)
    scissors.config(state=NORMAL)

rock = Button(root, padx=10, pady=10, command=lambda: choose("rock"), text='Rock')
paper = Button(root, padx=10, pady=10, command=lambda: choose("paper"), text='Paper')
scissors = Button(root, padx=10, pady=10, command=lambda: choose("scissors"), text='Scissors')

send = Button (root, padx=80, command=pc_choose, text='Start!')

scr.grid(row=0,column=0, columnspan=3)
rock.grid(row=1,column=0)
paper.grid(row=1,column=1)
scissors.grid(row=1,column=2)
send.grid(row=2,column=0,columnspan=3)

if __name__ == '__main__':
    root.mainloop()
    with open('./log.json','w') as f:
        f.write(str(log).replace('\'','"'))