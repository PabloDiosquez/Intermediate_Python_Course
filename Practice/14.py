# Exercise 14
# Write a program (function!) that takes a list and returns a new list that contains 
# all the elements of the first list minus all the duplicates.

# Extras:
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.

numberList = [1,1,1,1,2,3,2,2,4,5,]

def removeDuplicatesI(nList: list) -> list:
    noDuplicates = []
    for number in nList:
        if number not in noDuplicates:
            noDuplicates.append(number)
    return noDuplicates

def removeDuplicatesII(nList: list) -> list:
    return list(set(nList))

print(f'Original list: {numberList}')
print(f'List without duplicates: {removeDuplicatesI(numberList)}')
print(f'List without duplicates: {removeDuplicatesII(numberList)}')