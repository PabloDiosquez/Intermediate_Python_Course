# Exercise 2
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message 
# to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

import myFunctions

def even_check(number) -> str:
    result = 'ODD'
    if not number % 4:
        result = 'EVEN & MULTIPLE OF 4'
    elif not number % 2:
        result = 'EVEN'
    return result

def dividesTo(number, check):
    return not number % check
    
number = myFunctions.getInt('Enter a number:')
result = even_check(number)
print(f'Dear user, the number {number} is {result}')

number = myFunctions.getInt('Enter another number:')
check = myFunctions.getInt('Enter a number to divide the previous by:')

if dividesTo(number, check):
    print(f'{number} divides evenly by {check}')
else:
    print(f'{number} does not divides evenly by {check}')