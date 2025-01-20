storage=[[],[],[]]
while True:
    print(storage)
    print("Add to storage, remove from storage, or exit?")
    place=input()
    if place=="Add to storage":
        print("Which row do you want to add to?")
        row=int(input())-1
        print("What do you want to add?")
        adding=input()
        storage[row].append(adding)
    if place=="Remove from storage":
        print("Which row do you want to remove from?")
        row=int(input())-1
        print("what do you want to remove?")
        removing=input()
        storage[row].append(removing)
    if place=="Exit":
        exit(0)