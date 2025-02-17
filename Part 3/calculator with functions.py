def add(one,two,three):
    return one+two+three
def subtract(one,two,three):
    return one-two-three
def multiplication(one,two,three):
    return one*two*three
def division(one,two,three):
    return one/two/three
variable=True
while variable==True:
    one=int(input("What is the first number?"))
    two=int(input("What is the second number?"))
    three=int(input("What is the third number?"))
    operation=input("What operation would you prefer?")
    if operation=="add":
        print(add(one,two,three))
    elif operation=="subtract":
        print(subtract(one,two,three))
    elif operation=="multiplication":
        print(multiplication(one,two,three))
    elif operation=="division":
        print(division(one,two,three))
    else:
        print("Invalid Operation")
    runagain=input("Do you want to make another calculation?")
    if runagain=="no":
        variable=False