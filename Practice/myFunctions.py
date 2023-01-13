import random

def getInt(message):
    return int(input(f'{message} \n>>> '))

def getString(message):
    return input(f'{message} \n>>> ')

def numberRandomList(size=10) -> list:
    return list(set(random.sample(range(1,20),size)))

def turnOver(string: str) -> str:
    string = string.lower().replace(' ','')
    reverse = ''
    for index in range(len(string)-1,-1,-1):
        reverse += string[index]
    return reverse

def isPrime(number: int) -> bool:
    jumper = 2
    while number % jumper and jumper <= number//2:
        jumper +=1
    if number > 1 and jumper > number//2:
        return True
    return False