from queue import Queue
test=Queue()
test.push(4)
test.push(7)
test.push(21)
print(len(test))
print(test.peek())
print(test.pop())
print(test.pop())