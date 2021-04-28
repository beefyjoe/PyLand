import os
import time
import random

length = 38
height = 15


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

def fall(xpos,ypos,char):
    i = 0
    while ypos != height:
        time.sleep(.0625)
        AddPoint(xpos,ypos,"_")
        time.sleep(.0625)
        ypos += 1
        AddPoint(xpos,ypos,char)

def PLand(clr):
    print("                                                                  ")
    l = 0
    counter = 0
    while l != height: # prints each line
        print(''.join(pregen[counter:length+counter])) # all kinds of nonesense
        counter += length
        l += 1

def getpoint(x,y):
    
    return pregen[(x - 1) + ((y - 1) * length)]

def addpoint(x,y,char):
    position = (x - 1) + ((y - 1) * length)
    pregen[position] = char
    cls = lambda: os.system('cls')
    cls()
    PLand(0)

char = [
    "_"
]

gen(length,height,1)
addpoint(2,3,"x")
test = getpoint(2,2)
print(test)