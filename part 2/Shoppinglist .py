shop=[]
while True:
    print(shop)
    print("Add to the cart, remove from the cart, or exit?")
    variable=input()
    if variable=="Add to the cart":
        print("What do you want to add to the cart?")
        eat=input()
        shop.append(eat)
    if variable=="remove from the cart":
        print("What do you want to remove from cart?")
        note=input()
        if note in shop:
            shop.remove(note)
        else:
            print("Iten is not detected on the list.")
    if variable=="exit":
        exit(0)
