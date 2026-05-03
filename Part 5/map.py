class map:
    def __init__(self):
        self.keys=[]
        self.values=[]
    def add(self,key,value):
        self.values.appemd(value)
        self.keys.append(key)
    def get(self,key):
        for i in range(len(self.keys)):
            if self.keys[i]==key:
                return self.values[i]
