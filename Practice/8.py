# Exercise 8 
# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of 
# congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:
# βπΌ > βπΌ
# βπΌ > βπΌ
# βπΌ > βπΌ

import myFunctions
import random

def userWins(userChoice: str, computerChoice: str) -> bool:
    if userChoice == 'rock' and computerChoice == 'scissors' or userChoice == 'paper' and computerChoice == 'rock' or userChoice == 'scissors' and computerChoice == 'paper':
        return True
    return False 

def playGame():
    choiceList = ['rock','paper','scissors']
    userChoice = myFunctions.getString('Choose between Rock, Paper or Scissors:').lower()
    computerChoice = random.choice(choiceList)
    print(f'User choice: {userChoice}')
    print(f'Computer choice: {computerChoice}')
    if userChoice == computerChoice:
        print('ItΒ΄s a DRAW')
    elif userWins(userChoice, computerChoice):
        print('You WIN! ππΌ')
    else:
        print('You LOSE! π»')

while True:
    playGame()
    playerInput = myFunctions.getString('Continue playing (Y/N)?:')
    if playerInput.upper() != 'Y':
        break