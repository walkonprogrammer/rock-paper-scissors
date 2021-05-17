#!/bin/python3

# contains the code to import the function used in this project.
# randit is used to generate random numbers
from random import randint

# allow the player to choose Rock, Paper, Scissors by typing the letter 'r','p', or 's'
player = input('rock (r), paper(p) or scissors(s)?')

# print out what the player chose
#print(player, 'vs', end=' ')
# instead of saying print(player); add a new if statement to check which item the player chose and print out correct  character
if player == 'r':
  print('0', 'vs', end=' ') # adding the end='' at the end of print makes it end with a space instead of a new line

if player == 'p':
  print('__', 'vs', end=' ')

if player == 's':
  print('8<', 'vs', end=' ')

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
  print('0')
# add an alternative check using elif (aka else if)
# this condition will be checked if the first condition fails (if the computer didn't chose 1)
elif chosen == 2:
  computer = 'p'
  print('__')
# if the computer didn't choose 1 or 2 then it must have chosen 3
# use else (aka otherwise)
else:
  computer = 's'
  print('>8')

#print(computer)

# check the results
# add the code to see who won
# you will need to compare the player and computer variables to see who won
# if the are the same then it is a draw
if player == computer:
  print('DRAW!')

# create the case where the player chose rock 'r' but the computer did not
# if the computer chose scissors 's' then the player wins (roc beats scissors)
# if the computer chose paper 'p' then the computer wins  (paper beats rock)
# check the player choice and the computer choice using and

elif player == 'r' and computer == 's':
  print('Player Wins!')

elif player == 'r' and computer == 'p':
  print('Computer Wins!')

# create the case where the player chose paper 'p' but the computer did not

elif player == 'p' and computer == 'r':
  print('Player Wins!')

elif player == 'p' and computer == 's':
  print('Computer Wins!')

# lastly create the case where the player chose scissors 's' and the computer did not

elif player == 's' and computer == 'r':
  print('Computer Wins!')

elif player == 's' and computer == 'p':
  print('Player Wins!')

else:
  print('Huh?')
