#Guess the number

import random

number = random.randint(0,9)

svar = raw_input("Guess number: ")

while not svar.isdigit():
    svar = raw_input("You didn't enter a digit. Try again: ")

while int(svar) != number:
    if int(svar) < number:
        svar = raw_input("Your guess is too low. Guess again: ")
    elif svar > number:
        svar = raw_input("Your guess is too high. Guess again: ")
else: 
    print "Your guess is right! The number was " + str(number)
