import random, time
from tkinter import *

root = Tk()
root.title = 'Rock/Paper/Scissors'
root.config(padx=50,pady=50)

scr = Label(root, text='Welcome to the game!')

possible = ["Rock","Paper","Scissors"]

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
    pc_choice = random.choice(possible)
    try: compare();print(pc_choice)
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
    elif pc_choice == "Rock" and choice == 'Scissors':
        text = "You lose!"
    else:
        text = "You win!"
    now = time.strftime("%d/%m/%Y %H:%M:%S")
    scr.config(text=text)
    send.config(text='Again', command=reset)
    log.setdefault(now,[choice,pc_choice,text])

def reset():
    global choice
    try:del choice
    except:pass
    send.config(text='Start',command=pc_choose)
    scr.config(text='Choose a button')
    rock.config(state=NORMAL)
    paper.config(state=NORMAL)
    scissors.config(state=NORMAL)

rock = Button(root, padx=10, pady=10, command=lambda: choose("Rock"), text='Rock')
paper = Button(root, padx=10, pady=10, command=lambda: choose("Paper"), text='Paper')
scissors = Button(root, padx=10, pady=10, command=lambda: choose("Scissors"), text='Scissors')

send = Button (root, padx=80, command=pc_choose, text='Start!')

scr.grid(row=0,column=0, columnspan=3)
rock.grid(row=1,column=0)
paper.grid(row=1,column=1)
scissors.grid(row=1,column=2)
send.grid(row=2,column=0,columnspan=3)

if __name__ == '__main__':
    root.mainloop()
    with open('./log.json','w') as f:
        f.write(str(log).replace('\'','"').replace('], ','],\n  '))