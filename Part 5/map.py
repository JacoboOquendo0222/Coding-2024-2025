class map:
    def __init__(self):
        self.keys=[]
        self.values=[]
    def add(self,key,value):
        self.values.append(value)
        self.keys.append(key)
    def get(self,key):
        for i in range(len(self.keys)):
            if self.keys[i]==key:
                return self.values[i]
    def getkeys(self):
        return self.keys
    def getvalue(self):
        return self.values
    def contain(self,key):
        if key in self.keys:
            return True
        else:
            return False
    def __len__(self):
        return len(self.keys)