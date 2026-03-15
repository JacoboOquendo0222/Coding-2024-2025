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
    def remove(self,value):
        self.head=self.removenode(value,self.head)
    def removenode(self,value,node):
        if node==None:
            return None
        else:
            nodevalue=node.getvalue()
            if nodevalue==value:
                self.size-=1
                if node.getleft()==None and node.getright()==None:
                    return None
                elif node.getleft()==None:
                    return node.getright()
                elif node.getright()==None:
                    return node.getleft()
                else:
                    sucessor=node.getleft().maxvalue()
                    node.setvalue(sucessor.getvalue())     
                    sucessor.setvalue(nodevalue)
                    node.setleft(self.removenode(nodevalue,node.getleft()))
                    return node
            elif nodevalue>value:
                newleftnode=self.removenode(value,node.getleft())
                node.setleft(newleftnode)
                return node
            else:
                newrightnode=self.removenode(value,node.getright())
                node.setright(newrightnode)
                return node