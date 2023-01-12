# Exercise 6
# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

import myFunctions

def checkPalindrome(string: str) -> bool:
    return string == myFunctions.turnOver(string)

phrase = myFunctions.getString('Insert a phrase:').lower().replace(' ','')

if checkPalindrome(phrase):
    print('The phrase is a palindrome')
else:
    print('The phrase is NOT a palindrome')