class card:
    def __init__(self,value,suit):
        self.value=value
        self.suit=suit
    def __str__(self):
        end=str(self.value)+" of "+self.suit
        if self.value==1:
            end="Ace of "+self.suit     
        if self.value==11:
            end="Jack of "+self.suit   
        if self.value==12:
            end="Queen of "+self.suit
        if self.value==13:
            end="King of "+self.suit
        return end
    def __eq__(self,other):
        if self.value==other.value and self.suit==other.suit:
            return True
        else:
            return False
    def __gt__(self,other):
        if self.value>other.value:
            return True
        if self.value<other.value:
            return False
        if self.value==other.value:
            if self.suit=="clubs":
                return False
            if self.suit=="diamonds":
                if other.suit=="clubs":
                    return True
                else:
                    return False
            if self.suit=="hearts":
                if other.suit=="clubs"or other.suit=="diamonds":
                    return True
                else:
                    return False
            if self.suit=="spades":
                if other.suit=="clubs"or other.suit=="diamonds"or other.suit=="hearts":
                    return True
                else:
                    return False
                #clubs<diamonds<hearts<spades