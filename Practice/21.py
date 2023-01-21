# Implement a function that takes as input three variables, 
# and returns the largest of the three. Do this without using the Python max() function!

# The goal of this exercise is to think about some internals that Python normally 
# takes care of for us. All you need is some variables and if statements!

def maxTwoNumbers(num1,num2) -> int:
    if num1 >= num2: return num1
    return num2

def maxNumberI(num1,num2,num3) -> int:
    if num1 >= num2:
        maxNumber = num1
    else:
        maxNumber = num2
    if num3 >= maxNumber:
        maxNumber = num3
    return maxNumber

def maxNumberII(num1,num2,num3) -> int:
    return maxTwoNumbers(maxTwoNumbers(num1,num2),num3)

def maxNumberIII(num1,num2,num3) -> int:
    return sorted([num1,num2,num3])[2]

print(f'Max number is: {maxNumberI(2,11,9)}')
print(f'Max number is: {maxNumberII(2,11,9)}')
print(f'Max number is: {maxNumberIII(2,11,9)}')