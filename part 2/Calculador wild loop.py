variable=True
while variable==True:
    one=int(input("What is the first number?"))
    two=int(input("What is the second number?"))
    three=int(input("What is the third number?"))
    operation=input("What operation would you prefer?")
    if operation=="add":
        print(one+two+three)
    elif operation=="subtract":
        print(one-two-three)
    elif operation=="multiplication":
        print(one*two*three)
    elif operation=="division":
        print(one/two/three)
    else:
        print("Invalid Operation")
    runagain=input("Do you want to make another calculation?")
    if runagain=="no":
        variable=False