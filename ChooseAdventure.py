# Choose your own adventure game - Individual Python Projects --- 19th Dec 2020


import random
import time

def displayIntro():
    print('\nYour car broke down in your drive through the desert 2 days ago.')
    time.sleep(2)
    print('You have been walking across the sand dunes for what feels like forever with no roads or people in in sight.')
    time.sleep(2)
    print('\nYou close your eyes and pray to God that you will make it out of this situation alive.')
    time.sleep(2)
    print('You reopen your eyes and look to your feet.')
    time.sleep(1.5)
    print('\nYou find yourself now standing on a path branching in 2 different directions.')

    
def choosePath():
    path = ""
    while path != "1" and path != "2": # input validation
        path = input('\nWhich path will you take? 1 or 2?: ')


    return path    


def checkPath(chosenPath):
    print('You head down the path')
    time.sleep(1)
    print('The sun beams down harshly on your skin. You feel the dryness of your skin and your throat')
    time.sleep(1)
    print('Hours pass and you begin to doubt if you went down the correct path')
    

    correctPath = random.randint(1, 2)

    if chosenPath == str(correctPath):
        print('You notice what appears to be two figures in the distance')
        time.sleep(2)
        print('You break into the best jog you can manage in your exhausted, dehydrated state.')
        print('You see a man accompanied by a camel. You approach him and he offers you food and water.')
        time.sleep(1)
        print('You accept and ask him to help make your way back towards society')
        print('He walks you to a coles that was only 87 meters away.')
    else:
         print('You see what appears to be numberous sticks slowly circling you.')
         time.sleep(2)
         print('Those aren\'t sticks...')
         time.sleep(1.7)
         print('...')
         time.sleep(2)
         print('AHHHHHHH, THEY\'RE SNAKES!')
         time.sleep(1)
         print('You are attacked and killed by the snakes')
         
        

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice) # choice is equal to '1' or '2'.
    playAgain = input('Do you want to play again? (yes or y to continue: ')
