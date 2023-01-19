# Exercise 20
# Write a function that takes an ordered list of numbers (a list where the elements are in order 
# from smallest to largest) and another number. The function decides whether or not the given number 
# is inside the list and returns (then prints) an appropriate boolean.
# Extras:
# Use binary search.

import myFunctions

def binarySearch(ordList, number):
    left, right = 0, len(ordList)-1
    while left <= right:
        half = (left + right) // 2
        if ordList[half] == number:
            return True
        elif ordList[half] < number:
            left = half + 1
        elif ordList[half] > number:
            right = half - 1
    return False

if __name__ == '__main__':
    # orderedList = [0, 1, 3, 4, 5, 6, 7, 8, 9]
    orderedList = myFunctions.numberRandomList()
    orderedList.sort()
    number = myFunctions.getInt('Enter a number:')
    print(f'List: {orderedList}')
    if binarySearch(orderedList, number):
        print(f'The number {number} is in the list')
    else:
        print(f'The number {number} is NOT in the list')