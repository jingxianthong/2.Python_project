# this using the random funciton library to perfume 2 function. 

# The first funciton is (User) guess the number.
#  And the Second funciton is (Computer) guess the a number for you 

import random

def  guess(x):
    random_number = random.randint(1,x)

    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry , guess again. Too low.")
        elif guess >random_number:
            print("Sorry guess again. Too high.")

    print(f"Yeahh, congrats. you guess the number {random_number} correctly!!")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != "c":
        if low  !=  high:
            guess= random.randint(low,high)
        else:
            guess = low 
        
        feedback = input(F"Is {guess} too high(H) or too low (L), or Correct (C) : ").lower()
        if feedback == "h":
            high = guess - 1 
        elif feedback == "l":
            low  = guess + 1

    print(f"Yeahh, congrats.the computer guess the number {guess} correctly!!")

computer_guess(1000)