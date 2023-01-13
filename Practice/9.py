# Exercise 9 
# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low,
# too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import myFunctions
import random

def playGame():
    secretNumber = random.randint(1,9)
    attemptCounter = 0
    while True:
        userNumber = myFunctions.getInt('Guess the secret number from 1 to 9:')
        if userNumber == secretNumber:
            print('You WIN!👏🏼')
            break
        elif userNumber > secretNumber:
            print('Your guess was too high. Keep trying!')
            attemptCounter += 1
        else:
            print('Your guess was too low. Keep trying!')
            attemptCounter += 1
    print(f'Secret Number: {secretNumber}')
    print(f'Number of guesses: {attemptCounter}')

exit = False

while not exit:
    playGame()
    userInput = myFunctions.getString('Continue playing (type exit if you do not want to):')
    if userInput.lower() == 'exit':
        exit = True