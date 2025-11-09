import Deck
from Deck import deck
playerhand=[]
otherplayerhand=[]
pile=deck()
pile.shuffle()
for i in range(26):
    playerhand.append(pile.draw())
    otherplayerhand.append(pile.draw())
while not ((len(playerhand)==52)or(len(otherplayerhand)==52)):