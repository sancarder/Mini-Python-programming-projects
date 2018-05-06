#Dice rolling

import random

min = 1
max = 6
roll = "Y"

def roll_dice():
    number = random.randint(min, max)
    print number
    
while roll == "Y" or roll == "y":
    roll_dice()
    roll = raw_input("Roll dice again? Y/N: ")
