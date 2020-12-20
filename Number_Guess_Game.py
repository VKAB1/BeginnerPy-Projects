#Number Guesser Game - Indiv projects ----- 19th Dec 2020

import random


# name input and game explaination
print('Hello, This is the Number Guesser Game! Please input your name: ')
name = input()
print('Hello ' + name + '. Please try and guess a random number between 1-100. \nYou will have 6 chances.')


# Secret/random number
secNum = random.randint(1, 100)


# Sets the amount of guesses allowed
for guessesTaken in range(1,7):
    print('What is your guess?')
    guess = int(input())

    if guess < secNum:
        print('Too low, try again.')
    elif guess > secNum:
        print('Too high, try again.')

    else:
        break

    
if guess == secNum:
    print('Congratulations. You have guessed the number correctly.')

else:
    print('The secret number was ' + str(secNum) + '. Good try.') 
