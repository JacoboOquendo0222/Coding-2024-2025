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
while not ((len(playerhand)==52)or(len(otherplayerhand)==52)):
    playerhand.pop
    print("The amount of card player 1 has is",(len(playerhand)))
    print("The amount of card player 2 has is",(len(otherplayerhand)))
    print("the amount of card central pile has is",(len(centralpile)))
    centralpile.append(playerhand.pop())
    centralpile.append(otherplayerhand.pop())
    print("The card that you added is",(centralpile[-2]))
    print("The card that other player added is",(centralpile[-1]))
    if centralpile[-2]>centralpile[-1]:
        print("player 1 wins this round")
        playerhand.extend(centralpile)
        centalpile=[]
    elif centralpile[-2]<centralpile[-1]:
        print("player 2 wins this round")
        otherplayerhand.extend(centralpile)
        centralpile=[]
    elif centralpile[-2]==centralpile[-1]:
        print("War, nobody wins")
