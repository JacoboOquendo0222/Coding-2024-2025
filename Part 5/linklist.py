#Some methouds we need to put in the linklist is the string method, mabye the none function in the beggining of the code for then later we could decide on a good name
from linklistnode import node
class linklist:
    def __init__(self):
        self.size=0
        self.head=None
    def __len__(self):
        return self.size
    def getnode(self,position):
        start=self.head
        for i in range(position):
            start=node.nextnode(start)
        return start 
    def addnode(self,position,nodes):
        if position==0:
            node.setnextnode(nodes,self.head)  
            self.head=nodes
        else:
            add=node.getnode(self,position-1)
            node.setnextnode(nodes,add.nextnode())
            node.setnextnode(add,nodes)
    def add(self,position,value):
        adding=node(value)
        self.addnode(position,adding)
    def __str__(self):
        rode=""
        start=self.head
        for i in range(self.size):
            rode=rode+str(start)
            start=node.nextnode(start)
        return rode