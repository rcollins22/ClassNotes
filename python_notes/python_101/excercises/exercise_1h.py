""" Print the first 100 triangle numbers. What is a 
triangle number? Read this article to find out 
what triangle numbers are (https://www.mathsisfun.com/algebra/triangular-numbers.html) """
#---------------------------------------------------------------------------------------
""" var=1
result=1
print(var)
while result<= 100:
    result=var(var+1)
    print(result) """


#---------------------------------------------------------------------------------------
""" You will implement a guess-the-number game where the player has to try guessing
a secret number until they gets it right. For now, you will "hard code" the 
secret number to 5 (just set it to five like secret_number = 5). You will prompt
the player to enter a number again and again, each time comparing their input to 
the secret number. To to that, you will need to write a while loop. If they guess correctly, 
you will print "You win!", otherwise, you will prompt for a number again. """

""" nbr=5
guess=int(input("Guess the number:\n"))

while nbr != guess:
    guess=int(input('Wrong, Please try again:\n')) 
if nbr==guess:
    print("you must be Psychic!")
    exit() """
#-------------------------------------------------------------------------------------------------------
"""secret_number = 5                  ###SOMEONE ELSES' BROKEN CODE###
greet = "I am thinking of a number between one and ten.\n"
print(greet)
ask_num = int(input("What is the number?\n"))

 while secret_number != ask_num:
    if ask_num == secret_number:
        print("Yes, You win")
        exit()
    if ask_num != secret_number:
        ask_num = int(input("What is the number?\n"))
        print("No, You Lose")
        print(ask_num)
    if int(ask_num) < 1 or int(ask_num) > 10:
        print("Please enter a number between 1 and 10")
    else:
        print(ask_num) """




""" secret_number = 5           ####MY SOLUTION TO THEIR CODE#####
greet = "I am thinking of a number between one and ten.\n"
print(greet)
ask_num = int(input("What is the number?\n"))

while secret_number != ask_num:
    if ask_num != secret_number:
        print("No, You Lose")
        ask_num = int(input("What is the number?\n"))
    if int(ask_num) < 1 or int(ask_num) > 10:
        print("Please enter a number between 1 and 10")
    else:
        print(ask_num)
if ask_num == secret_number:
        print("Yes, You win")
        exit()  """

#---------------------------------------------------------------------------------------
'''Improve your game to provide the player with a high-or-low hint.'''

"""nbr=5
guess=int(input("Guess the number:\n"))

while nbr != guess:
    if guess > nbr:
        print("\ntoo high\n")
    if guess < nbr:
        print('\ntoo low\n')
    guess=int(input('Wrong, Please try again:\n')) 

if nbr==guess:
    print("you must be Psychic!")
    exit() """
#---------------------------------------------------------------------------------------
""" Instead of hard-coding the secret number to 5 now, you will generate the secret number 
using a random number generator provided by Python, so that even you, the programmer, cannot
know the secret number before hand.  """

"""import random
nbr= random.randint(1, 10)                ####GENERATES A RANDOM NUMBER####
guess=int(input("Guess the number:\n"))


while nbr != guess:
    if guess > nbr:
        print("\ntoo high\n")
    if guess < nbr:
        print('\ntoo low\n')
    guess=int(input('Wrong, Please try again:\n')) 

if nbr==guess:
    print("you must be Psychic!")
    exit() """
#---------------------------------------------------------------------------------------
 """Limit the number of guesses the player has to 5. If he cannot guess the number
  within 5 guesses, he losses."""

import random
nbr= random.randint(1, 10)                ####GENERATES A RANDOM NUMBER####
guess=int(input("Guess the number:\n"))
GUESS_LEFT=4

while nbr != guess:
    if guess > nbr:
        print("\ntoo high\n")
    if guess < nbr:
        print('\ntoo low\n')
    guess=int(input('Wrong, Please try again:\n')) 

if nbr==guess:
    print("you must be Psychic!")
    exit() 


