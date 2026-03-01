from Binarynode import Binarynode
class tree:
    def __init__(self):
        self.size=0
        self.head=None
    def addnode(self,head,nodes):
        headvalue=head.getvalue()
        nodevalue=nodes.getvalue()
        if headvalue>=nodevalue:
            leftnode=head.getleft()
            if leftnode is None:
                self.size+=1
                head.setleft(nodes)
            else:
                self.addnode(leftnode,nodes)
        else:
            rightnode=head.getright()
            if rightnode is None:
                self.size+=1
                head.setright(nodes)
            else:
                self.addnode(rightnode,nodes)
    def add(self,value):
        binode=Binarynode(value)
        if self.head is None:
            self.size+=1
            self.head=binode
        else:
            self.addnode(self.head,binode)
    def __len__(self):
        return self.size
    def aslist(self):
        return self.head.aslist()
