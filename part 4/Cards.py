class card:
    def __init__(self,value,suit):
        self.value=value
        self.suit=suit
    def toString(self):
        end=str(self.value)+" of "+self.suit
        if self.value==1:
            end=" Ace of "+self.suit     
        if self.value==11:
            end=" Jack of "+self.suit   
        if self.value==12:
            end=" Queen of "+self.suit
        if self.value==13:
            end=" King of "+self.suit
        return end
