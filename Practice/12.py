# Exercise 12
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new
# list of only the first and last elements of the given list. For practice, write this code inside a function

from myFunctions import numberRandomList

def firstAndLast(nList: list) -> list:
    return [nList[0],nList[-1]]

numberList = numberRandomList(14)
print(f'Number list: {numberList}')
print(f'First and Last list: {firstAndLast(numberList)}')