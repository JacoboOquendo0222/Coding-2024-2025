import random
from random import randint
number=randint(1,1000)
tries=0
while tries<10:
    tries=tries+1
    print("Guess",tries)
    guess=int(input("What is your guess?"))
    if guess>number:
        print("Guess is too high")
    elif guess<number:
        print("Guess is too low")
    elif guess==number:
        print("You win")
        exit(0)
print("You lose")
print("The number is",number)