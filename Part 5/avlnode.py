from Binarynode import Binarynode
class nodeavl(Binarynode):
    def __init__(self,value):
        super().__init__(value)
        self.maxheight=0
        self.balancefactor=0
    def update(self):
        leftheight=-1
        rightheight=-1
        if not self.left==None:
            leftheight=self.left.getmaxheight()
        if not self.right==None:
            rightheight=self.right.getmaxheight()
        self.maxheight=1+max(leftheight,rightheight)
        self.balancefactor=rightheight-leftheight
    def getmaxheight(self):
        return self.getmaxheight
    def getbalancefactor(self):
        return self.getbalancefactor