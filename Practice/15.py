# Exercise 15
# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order. 
# For example, say I type the string:

# My name is Michele
# Then I would see the string:

# Michele is name My
# shown back to me.

import myFunctions

def reverseString(string: str) -> str:
    splitString = string.split()
    splitString.reverse()
    return ' '.join(splitString)

# One-line solution
def reverseStringII(string: str):
    return ' '.join(string.split(' ')[::-1])
    
inputString = myFunctions.getString('Insert long text here:')
print(f'Reverse: {reverseString(inputString)}')
print(f'One-liner: {reverseStringII(inputString)}')