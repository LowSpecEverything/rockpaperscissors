import time, random

possible = ["Rock","Paper","Scissors"]
log = {}

for n,choice in enumerate(possible):
    print(f'{n+1} - {choice}')

choice = possible[int(input('Your choice (1-3): ')) - 1]

pc_choice = random.choice(possible)

if pc_choice == choice:
        text = "Tied!"
elif possible.index(pc_choice) > possible.index(choice):
    text = "You lose!"
elif pc_choice == "Rock" and choice == 'Scissors':
    text = "You lose!"
else:
    text = "You win!"
print(f'{text} Computer chose {pc_choice}')

now = time.strftime("%d/%m/%Y %H:%M:%S")
log.setdefault(now,[choice,pc_choice,text])
with open('log2.json', 'w') as f:
    f.write(str(log).replace('\'','"').replace('], ','],\n  '))