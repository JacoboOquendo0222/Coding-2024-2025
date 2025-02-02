board=[["/","/","/"],["/","/","/"],["/","/","/"]]
one="x"
count=0
while True:
    for i in range(3):
        print(board[i])
    if count==9:
        print("Draw")
        exit(0)
    print(one+" It is your turn")
    print("Which row do you want to play in?")
    row=int(input())-1
    print("which colum do you want to play in?")
    colum=int(input())-1
    if not "/"==board[row][colum]:
        print("Space is already taken, dont cheat.")
        continue
    board[row][colum]=one
    if board[0][0]==one and board[0][1]==one and board[0][2]==one:
        print("You win",one)
        exit(0)
    if board[1][0]==one and board[1][1]==one and board[1][2]==one:
        print("You win",one)
        exit(0)
    if board[2][0]==one and board[2][1]==one and board[2][2]==one:
        print("You win",one)
        exit(0)
    if board[0][0]==one and board[1][0]==one and board[2][0]==one:
        print("You win",one)
        exit(0)
    if board[0][1]==one and board[1][1]==one and board[2][1]==one:
        print("You win",one)
        exit(0)
    if board[0][2]==one and board[1][2]==one and board[2][2]==one:
        print("You win",one)
        exit(0)
    if board[0][0]==one and board[1][1]==one and board[2][2]==one:
        print("You win",one)
        exit(0)
    if board[0][2]==one and board[1][1]==one and board[2][0]==one:
        print("You win",one)
        exit(0)
    if one=="x":
        one="o"
    else:
        one="x"
    count=count+1