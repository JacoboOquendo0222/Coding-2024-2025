class Binarynode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
    def getvalue(self):
        return self.value
    def getleft(self):
        return self.left
    def getright(self):
        return self.right
    def setleft(self,abdominal):
        self.left=abdominal
    def setright(self,abdominal):
        self.right=abdominal
    def setvalue(self,value):
        self.value=value
    def __str__(self):
        return str(self.value)

