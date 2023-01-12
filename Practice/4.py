# Exercise 4
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides 
# evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

import myFunctions

def generateDivisorList(number: int) -> list:
    divisorList = []
    for d in range(1,number+1):
        if not number % d:
            divisorList.append(d)
    print(f'List of divisors for number {number}:',end=' ')
    return divisorList

print(generateDivisorList(myFunctions.getInt('Insert a number: ')))