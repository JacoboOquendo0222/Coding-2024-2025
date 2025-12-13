class Stack:
    def __init__(self):
        self.grouping=[]
    def __len__(self):
        return len(self.grouping)
    def push(self,arrange):
        (self.grouping.append(arrange))
    def peek(self):
        return self.grouping[-1]
    def pop(self):
        return self.grouping.pop(-1)