# To create a hangman game in Python, we will use the following steps.

# First, we will ask for the name of the user. We will take the user input using the input() method. After execution, the input() method takes the input from the user and returns a string.
# Next, we will select a word and ask the user to start guessing the characters in the word.
# We will also define the maximum number of attempts the user can take.
# Now, we will use a while loop to repeatedly ask the user to guess the character until the attempts are exhausted.
# Inside the while loop, if the user guesses the correct character. We will include it in the response. Otherwise, we will notify the user that they made a mistake.
# If the user is able to guess all the characters of the word within the maximum number of attempts, they win the game.
# If the user exhausts all their attempts before guessing the entire word, they lose.

import random
from words import words
import string 

def getValidWord(words):
    while True:
        word = random.choice(words)
        if '-' not in word and  ' ' not in word:
            return word.upper()

def hangman():
    word = getValidWord(words)
    wordLetters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    usedLetters = set() # what the user has guessed

    lives = 6

    # getting user input
    while len(wordLetters) > 0 and lives > 0:
        # letters used 
        print(f'You have used these letters: {usedLetters}')

        # what current word is (ie W - R D)
        wordList = [letter if letter in usedLetters else ' - ' for letter in word]
        print(f'Current word: ', ' '.join(wordList))


        userLetter = input('Guess a letter: ').upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
                print()
            else:
                lives -= 1
                print(f'Your letter {userLetter} is not in the word.')
        elif userLetter in usedLetters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again.')
    
    if lives == 0:
        print(f'You died, sorry. The word was {word} 😕')
    else:
        print('You guessed the word! 👏🏼')

if __name__ == '__main__':
    hangman()