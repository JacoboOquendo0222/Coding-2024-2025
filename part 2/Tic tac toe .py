board=[["/","/","/"],["/","/","/"],["/","/","/"]]
one="x"
while True:
    for i in range(3):
        print(board[i])
    print(one+" It is your turn")
    print("Which row do you want to play in?")
    row=int(input())-1
    print("which colum do you want to play in?")
    colum=int(input())-1
    board[row][colum]=one
    if one=="x":
        one="o"
    else:
        one="x"