# Exercise 5
# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are 
# common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:
# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import myFunctions

def commonList(nList1, nList2) -> list:
    commonList = []
    for number in nList1:
        if number in nList2 and number not in commonList:
            commonList.append(number)
    return commonList

randomList1 = myFunctions.numberRandomList()
randomList2 = myFunctions.numberRandomList(12)

print(f'randomList1: {randomList1}')
print(f'randomList2: {randomList2}')
print(f'List of common elements between both lists (no duplicates ✌🏼): {commonList(randomList1,randomList2)}')