from time import sleep
from random import randint
import Deck
from Deck import deck
playerhand=[]
otherplayerhand=[]
pile=deck()
pile.shuffle()
centralpile=[]
for i in range(26):
    playerhand.append(pile.draw())
    otherplayerhand.append(pile.draw())
while True:
    sleep(1.5)
    playerhand.pop
    print("The amount of card player 1 has is",(len(playerhand)))
    print("The amount of card player 2 has is",(len(otherplayerhand)))
    print("the amount of card central pile has is",(len(centralpile)))
    centralpile.append(playerhand.pop(randint(0,len(playerhand)-1)))
    centralpile.append(otherplayerhand.pop(randint(0,len(otherplayerhand)-1)))
    print("The card that you added is",(centralpile[-2]))
    print("The card that other player added is",(centralpile[-1]))
    if centralpile[-2].value>centralpile[-1].value:
        print("player 1 wins this round")
        playerhand.extend(centralpile)
        centralpile=[]
    elif centralpile[-2].value<centralpile[-1].value:
        print("player 2 wins this round")
        otherplayerhand.extend(centralpile)
        centralpile=[]
    elif centralpile[-2].value==centralpile[-1].value:
        print("War, nobody wins")
    if len(playerhand)==0:
        print("Player 2 is the winner")
        break
    if len(otherplayerhand)==0:
        print("Player 1 is the winner")
        break
