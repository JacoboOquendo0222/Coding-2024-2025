class node:
    def __init__(self,value):
        self.value=value
        self.next=None
    def __str__(self):
        return str(self.value)
    def nextnode(self):
        return(self.next)
    def setnextnode(self,next):
        self.next=next