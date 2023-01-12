# Exercise 3
# Take a list, say for example this one:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this 
# list in it and print out this new list.
# Ask the user for a number and return a list that contains only elements from the original list a that are
# smaller than that number given by the user.

import myFunctions

def lowerThanN(nList: list, input=5) -> list:
    lowerThanNList = []
    for number in nList:
        if number < input:
            lowerThanNList.append(number)
    return lowerThanNList

numberList = myFunctions.numberRandomList()
print(numberList)

inputNumber = myFunctions.getInt('Enter a number:')

print(f'List of numbers lower than 5: {lowerThanN(numberList)}')
print(f'List of numbers lower than {inputNumber}: {lowerThanN(numberList, inputNumber)}')