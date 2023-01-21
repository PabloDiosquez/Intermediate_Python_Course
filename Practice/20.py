# Exercise 23
# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. 
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a 
# list of happy numbers up to 1000.

# (If you forgot, prime numbers are numbers that can’t be divided by any other number. 
# And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. 
# The explanation is easier with an example, which I will describe below.)

def fromFileToList(filename):
    with open(filename, mode='r') as file:
        return file.readlines()

def overLapList(nList1, nList2):
    overLapList = []
    for number in nList1:
        if number in nList2:
            overLapList.append(number)
    return overLapList

primesList = fromFileToList('Practice\primenumbers.txt')
happyList = fromFileToList('Practice\happynumbers.txt')

print(overLapList(primesList,happyList))