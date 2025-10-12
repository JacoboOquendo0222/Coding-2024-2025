from Cards import card
from random import randint
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
    def shuffle(self):
        mix=[]
        while len(self.decks)>0:
            discard=randint(0, len(self.decks)-1)
            red=self.decks.pop(discard)
            mix.append(red)
        self.decks=mix