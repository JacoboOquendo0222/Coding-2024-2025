import random
from random import randint
print("Rock, Paper, or Scissors")
choise=input("").lower()
number=randint(1,3)
if number==(1):
    computerchoise="rock"
if number==(2):
    computerchoise="paper"
if number==(3):
    computerchoise="scissors"
print("cpu choise",computerchoise)
if choise==("rock") and computerchoise==("rock"):
    print("It was a tie")
if choise==("rock") and computerchoise==("scissors"):
    print("You win")
if choise==("rock") and computerchoise==("paper"):
    print("You lose")
if choise==("paper") and computerchoise==("paper"):
    print("It was a tie")
if choise==("paper") and computerchoise==("rock"):
    print("You win")
if choise==("paper") and computerchoise==("scissors"):
    print("You lose")
if choise==("scissors") and computerchoise==("scissors"):
    print("It was a tie")
if choise==("scissors") and computerchoise==("paper"):
    print("You win")
if choise==("scissors") and computerchoise==("rock"):
    print("You lose")