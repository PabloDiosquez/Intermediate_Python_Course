# Exercise 22
# Given a .txt file that has a list of a bunch of names, count how many of each name there are 
# in the file, and print out the results to the screen. I have a .txt file for you, if you want to use it!

def count_names(filename):
    names = {}
    with open(filename) as file:
        lines = file.readlines()
        for name in lines:
            if name in names.keys():
                names[name] += 1
            else:
                names[name] = 1
    return names

print(count_names('Practice\_nameslist.txt'))