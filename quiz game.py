score=0
print("What temperature will water will start to freeze?")
print("a 9 celcius b -5 celcius c 0 celcius d 33 celcius")
answer=input()
if answer=="c":
    print("correct")
    score=score+1
else:
    print("incorrect")
print("Where is Sleepy Hollow?")
print("a c-town b New York c California d Canada")
answer=input()
if answer=="b":
    print("correct")
    score=score+1
else:
    print("incorrect")
print("Where is Paris located?")
print("a Russia b England c Denmark d France")
answer=input()
if answer=="d":
    print("correct")
    score=score+1
else:
    print("incorrect")
print(score,"out of 3")