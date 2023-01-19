# Exercise 18
# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
# For every digit that the user guessed correctly in the correct place, they have a “cow”. 
# For every digit the user guessed correctly in the wrong place is a “bull.” 
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
# Once the user guesses the correct number, the game is over. Keep track of the number of guesses 
# the user makes throughout the game and tell the user at the end.

# Say the number generated by the computer is 1038. An example interaction could look like this:

#   Welcome to the Cows and Bulls Game! 
#   Enter a number: 
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull
#   ...
# Until the user guesses the number.

import random
import myFunctions

def digits(number: int) -> list:
    nList = []
    while number > 0:
        nList.append(number%10)
        number = number//10
    nList.reverse()
    return nList

def compareNumber(secretNumber, userNumber):
    cowbull = {
    'cows': 0,
    'bulls': 0
    }
    secretList = digits(secretNumber)
    digitsList = digits(userNumber)
    for i in range(len(secretList)):
        if digitsList[i] == secretList[i]:
            cowbull['bulls'] += 1
        elif digitsList[i] in secretList:
            cowbull['cows'] += 1
    return cowbull
   

def playGame():
    playing = True
    print('''Welcome to the Cows 🐮 and Bulls ♉ Game!
    I will generate a number, and you have to guess the numbers one digit at a time.
    For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.
    The game ends when you get 4 bulls!
    Type "exit" at any prompt to exit.
    ''')
    secretNumber = random.randint(1000,9999)
    print(secretNumber)
    guesses = 0
    while playing:
        userInput = myFunctions.getString('Give me your best guess!:')
        if userInput == 'exit': break
        result = compareNumber(secretNumber,int(userInput))
        guesses += 1
        cows = result.get('cows')
        bulls = result.get('bulls')
        print(f'Cows: {cows}, Bulls: {bulls}')
        if result['bulls'] == 4:
            print(f'You win the game after {guesses} guesses 🎉. The number was {secretNumber} ')
            playing = False
        else:
            print('Your guess isn´t quite right, try again!') 

if __name__ == '__main__':
    playGame()