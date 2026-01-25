#Some methouds we need to put in the linklist is the string method, mabye the none function in the beggining of the code for then later we could decide on a good name
from linklistnode import node
class linklist:
    def __init__(self):
        self.size=0
        self.head=None
    def __len__(self):
        return self.size
    def addnode(self,position,nodes):
        if position==0:
            node.setnextnode(nodes,self.head)  
            self.head=nodes

