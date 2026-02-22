from Binarynode import Binarynode
class tree:
    def __init__(self):
        self.size=0
        self.head=None
    def addnode(self,head,nodes):
        if head is None:
            self.size+=1
            head=nodes
        else:
            headvalue=head.getvalue()
            nodevalue=nodes.getvalue()
            if headvalue>=nodevalue:
                leftnode=head.getleft()
                self.addnode(leftnode,nodes)
            else:
                rightnode=head.getright()
                self.addnode(rightnode,nodes)
    def add(self,value):
        binode=Binarynode(value)
        self.addnode(self.head,binode)
    def __len__(self):
        return self.size
