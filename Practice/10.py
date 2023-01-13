# Exercise 10
# This week’s exercise is going to be revisiting an old exercise (see Exercise 5), 
# except require the solution in a different way.

# Take two lists, say for example these two:

# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common 
# between the lists (without duplicates). Make sure your program works on two lists of different sizes. 
# Write this in one line of Python using at least one list comprehension. 

# Extra:
# Randomly generate two lists to test this.

import myFunctions

randomList1 = myFunctions.numberRandomList()
randomList2 = myFunctions.numberRandomList(8)

commonList = list(set([number for number in randomList1 if number in randomList2]))

print(f'List 1: {randomList1}')
print(f'List 2: {randomList2}')
print(f'Common list: {sorted(commonList)}')