# Dice Rolling simulator ----- 20th Dec 2020

import random 

def simulate_dice():
    rollDice = random.randint(1, 6)
    print(rollDice)
    
    
again = True
while again:
    simulate_dice()

    another_roll = input('Want to roll again: ')
    if another_roll.lower().strip() == 'yes' or another_roll.lower().strip() =='y':
        continue
    else:
        print('Ok, stopping now')
        break

    
# Did most of this myself but then ran into an issue and redid everything using a guide
# GUIDE: https://datascienceunlimited.tech/step-by-step-coding-a-dice-roll-simulator-in-python/
