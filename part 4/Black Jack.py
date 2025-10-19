from Deck import deck
def values(playerhand):
    totalvalue=(0)
    for card in playerhand:
        if card.value<=10:
            totalvalue=totalvalue+card.value
        else:
            card.value>10
            totalvalue=totalvalue+10
    return totalvalue
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
    print("My first card is:"+str(dealerhand[0]))
    playerturn=True
    while playerturn==True:
        for card in playerhand:
            print(card)
    break