board=[["/","/","/","/","/","/","/"],["/","/","/","/","/","/","/"],["/","/","/","/","/","/","/"],["/","/","/","/","/","/","/"],["/","/","/","/","/","/","/"],["/","/","/","/","/","/","/"]]
one="x"
count=0
while True:
    for i in range(6):
        print (board[i])
    if count==42:
        print("Draw")
        exit(0)
    print(one+" It is your turn")
    print("which colum do you want to play in?")
    colum=int(input())-1
    row=5
    while True:
        if row==-1:
            break
        if "/"==board[row][colum]:
            board[row][colum]=one
            break
        else:
            row=row-1
    if row==-1:
        print("Colum is already full.")
        continue
    for r in range(6):
        for c in range(4):
           if board[r][c]==one:
                counting=1
                for o in range(1,4):
                   if board[r][o+c]==one:
                    counting+=1
                if counting==4:
                    print("You win",one)
                    exit(0)
    for r in range(3):
        for c in range(7):
           if board[r][c]==one:
                counting=1
                for o in range(1,4):
                   if board[o+r][c]==one:
                    counting+=1
                if counting==4:
                    print("You win",one)
                    exit(0)
    for r in range(3):
        for c in range(4):
           if board[r][c]==one:
                counting=1
                for o in range(1,4):
                   if board[o+r][o+c]==one:
                    counting+=1
                if counting==4:
                    print("You win",one)
                    exit(0)
    for r in range(3):
        for c in range(3,7):
           if board[r][c]==one:
                counting=1
                for o in range(1,4):
                   if board[o+r][c-o]==one:
                    counting+=1
                if counting==4:
                    print("You win",one)
                    exit(0)
    if one=="x":
        one="o"
    else:
        one="x"
    count=count+1
