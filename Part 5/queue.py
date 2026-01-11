class Queue:
    def __init__(self):
        self.lasting=[]
    def __len__(self):
        return len(self.lasting)
    def push(self,arrange):
        (self.lasting.append(arrange))
    def peek(self):
        return self.lasting[0]
    def pop(self):
        return self.lasting.pop(0)
        
