from Cards import card
class deck:
    def __init__(self):
        self.decks=[]
        for value in range(1,14):
            self.decks.append(card(value,suit="clubs"))
            self.decks.append(card(value,suit="diamonds"))
            self.decks.append(card(value,suit="hearts"))
            self.decks.append(card(value,suit="spades"))
    def __str__(self):
        carta=""
        for string in self.decks:
            carta+=str(string)
            carta+="\n"
        return carta
    def __len__(self):
        return len(self.decks)
    def draw(self):
        return self.decks.pop()