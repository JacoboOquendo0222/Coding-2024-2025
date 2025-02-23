import random
from random import randint
playerboard=[["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"]]
computerboard=[["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"]]
guessingboard=[["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"],["/","/","/","/","/","/","/","/","/","/"]]
def printboard(board):
    for i in range(10):
        print(board[i])
array=[5,4,3,3,2]
def playingship(board,shipsize,row,comlum,horizontaly,verticaly):
    if horizontaly==True:
        for i in range(shipsize):
            board[row][i+comlum]="m"
    if verticaly==True:
        for i in range(shipsize):
            board[i+row][comlum]="m"
for i in array:
    printboard(playerboard)
    horizontaly=False
    verticaly=False
    print("Your placing ",i," size ship")
    print("Do you want the ship horizontaly or verticaly?")
    horizontaly_or_verticaly=input()
    if horizontaly_or_verticaly=="horizontaly":
        horizontaly=True
    if horizontaly_or_verticaly=="verticaly":
        verticaly=True
    print("Which row do you want to place your ship?")
    row=int(input())-1
    comlum=int(input())-1
    playingship(board=playerboard,shipsize=i,row=row,comlum=comlum,horizontaly=horizontaly,verticaly=verticaly)
printboard(playerboard)