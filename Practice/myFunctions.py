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