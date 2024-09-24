#Rock Paper Scissors
#2 inputs, output who wins
from random import choice

player = ''#empty variable

invalid = True

while invalid:
    player = input("Enter your choice of (rock, paper, scissors): ")
    if player in{'rock', 'paper', 'scissors'}:
        invalid = False

cpu = choice(['rock', 'paper', 'scissors'])
print(f"CPU has chosen {cpu}.")
if cpu == player:
    print("Tie Game")
elif player == 'rock':
    if cpu == 'paper':
        print("You Lose")
    else:
        print('You Win')
elif player == 'paper':
    if cpu == 'scissors':
        print("You Lose")
    else:
        print('You Win')
else:
    if cpu == 'rock':
        print("You Lose")
    else:
        print('You Win')