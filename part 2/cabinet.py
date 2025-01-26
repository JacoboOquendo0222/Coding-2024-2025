storage=[[],[],[]]
while True:
    print(storage)
    print("Add to storage, remove from storage, or exit?")
    place=input()
    if place=="Add to storage":
        row=0-1
        while row <0 or row >2:
            print("Which row do you want to add to?")
            row=int(input())-1
        print("What do you want to add?")
        adding=input()
        storage[row].append(adding)
    if place=="Remove from storage":
        row=0-1
        while row <0 or row >2:
            print("Which row do you want to remove from?")
            row=int(input())-1
        print("what do you want to remove?")
        removing=input()
        if removing in storage[row]:
            storage[row].remove(removing)
        else:
            print("Item is not dectected on the list.")
    if place=="Exit":
        exit(0)