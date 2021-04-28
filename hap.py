import random

length = 5
height = 5


def gen(x, y, times):
    repeat = 0
    while repeat != times: # repeats depending on how many times you tell it too
        i = 0
        global pregen
        pregen = []
        
        while i != x * y: # gets the amount of charectors needed to create the square
            ran = random.randint(0,len(char) - 1)
            pregen.append(char[ran]) # adds a charector
            i += 1
        l = 0

        counter = 0
        while l != y: # prints each line
            print(''.join(pregen[counter:x+counter])) # all kinds of nonesense
            counter += x
            l += 1
        repeat += 1

def PLand(clr):
    l = 0
    counter = 0
    while l != height: # prints each line
        print(''.join(pregen[counter:length+counter])) # all kinds of nonesense
        counter += length
        l += 1

char = [
    "_",
    "-",
    "^",
    "O"
]

gen(length,height,1)

