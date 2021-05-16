#!/bin/python3

# contains the code to import the function used in this project.
# randit is used to generate random numbers
from random import randint

# allow the player to choose Rock, Paper, Scissors by typing the letter 'r','p', or 's'
player = input('rock (r), paper(p) or scissors(s)?')

# print out what the player chose
print(player, 'vs', end=' ')

# use the randint function to generate a random number to decide between rock, paper, and scissors
# chosen is randomly set to either 1, 2 or 3
chosen = randint(1,3)
#print(chosen) 
# remove the printing out of the random number that the computer chose so that we can print the letter

# we will choose that 1 = rock(r), 2 = paper(p), 3 = scissors(s)
# use if to check if the chosen number is 1
# == is used to see if 2 things are the same
if chosen == 1:
  computer = 'r' # set computer to 'r' inside the if (using indentation)
# add an alternative check using elif (aka else if)
# this condition will be checked if the first condition fails (if the computer didn't chose 1)
elif chosen == 2:
  computer = 'p'
# if the computer didn't choose 1 or 2 then it must have chosen 3
# use else (aka otherwise)
else:
  computer = 's'

print(computer)
