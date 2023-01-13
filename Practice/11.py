# Exercise 11
# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors).

import myFunctions

number = myFunctions.getInt('Insert a number: ')
if myFunctions.isPrime(number):
    print(f'The number {number} is prime!')
else:
    print(f'The number {number} NOT is prime!')