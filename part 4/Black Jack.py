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
    print("My first cards is:"+str(dealerhand[0]))
    playerturn=True
    print("Your cards are:")
    while playerturn==True:
        for card in playerhand:
            print(card)
        value=values(playerhand)
        print("Your value is", value)
        if value>=21:
            playerturn=False
        else:
            print("Do you want to Hit or Stand")
            Hit=input().lower()
            if Hit=="hit":
                playerhand.append(clubs.draw())
            if Hit=="stand":
                playerturn=False
    while values(dealerhand)<17:
        dealerhand.append(clubs.draw())
    for card in dealerhand:
        print(card)
    dealervalue=values(dealerhand)
    if dealervalue>21:
        if value>21:
            print("Tie")
    break
