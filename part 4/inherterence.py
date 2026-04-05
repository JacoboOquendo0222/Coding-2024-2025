from Cards import card
class procard(card):
    def __init__(self,value,suit):
        super().__init__(value,suit)
        self.timesplayed=0
    def play(self):
        self.timesplayed+=1
    def gettimesplayed(self):
        return self.timesplayed