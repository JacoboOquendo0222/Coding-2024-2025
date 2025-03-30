def hanoi(disk,start,middle,end):
    if disk==0:
        return
    else:
        hanoi(disk-1,start,end,middle)
        print("Move the disk from the",start,"to the",end)
        hanoi(disk-1,middle,start,end)
towers=int(input())
hanoi(towers,1,2,3)