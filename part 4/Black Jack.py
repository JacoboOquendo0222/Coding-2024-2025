from Deck import deck
clubs=deck()
clubs.shuffle()
playing=True
while playing==True:
    playerhand=[]
    dealerhand=[]
    playerhand.append(clubs.draw())
    dealerhand.append(clubs.draw())
    playerhand.append(clubs.draw())
    dealerhand.append(clubs.draw())
print("My first card is:"+dealerhand[0])