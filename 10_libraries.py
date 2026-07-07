# import random
from random import choice, randint, shuffle
from statistics import mean, median

from sys import argv, exit

dice = choice([1,2,3,4,5,6])
ch1 = randint(2,45)

cards = ["jack", "queen", "king"]
shuffle(cards)
print(ch1)
print(cards)



grades = [67,89,64,90,98]
print(mean(grades))

# argv[0] is name of the program

try:
    print("hello my name is", argv[1])
except:
    exit("too few arguments")
