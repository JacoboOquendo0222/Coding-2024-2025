def insertion_sort(placements):
    for io in range(0,len(placements)):
        for iae in range(io,-0,-1):
            if placements[iae]<placements[iae-1]:
                stuff=placements[iae]
                placements[iae]=placements[iae-1]
                placements[iae-1]=stuff
            else:
                break    
def sorting(placements):
    for o in range(0,len(placements)):
        finding=o
        for i in range(o,len(placements)):
            if placements[i]<placements[finding]:
                finding=i
        stuff=placements[o]
        placements[o]=placements[finding]
        placements[finding]=stuff
def bubble_sort(placements):
    for oi in range(0,len(placements)):
        for oie in range(0,len(placements)-1):
            if placements[oie]>placements[oie+1]:
                stuff=placements[oie+1]
                placements[oie+1]= placements[oie]
                placements[oie]=stuff
def merge(placements,start,end):
    middle=int((start+end)/2)
    inside=[]
    location,safe=start,middle+1
    while location<middle+1 and safe<end+1:
        if placements[location]>placements[safe]:
            inside.append(placements[safe])
            safe=safe+1
        else:
            inside.append(placements[location])
            location=location+1
    while location<middle+1:
        inside.append(placements[location])       
        location=location+1
    while safe<end+1:
        inside.append(placements[safe])
        safe=safe+1
    print(inside)
    for ai in range(0,len(inside)):
        placements[start+ai]=inside[ai]
def quicksort(placements,start,end):
    if end-start<3:
        if placements[start]>placements[end]: 
            stuff=placements[start]
            placements[start]= placements[end]
            placements[end]=stuff
    else:
        middle=partition(placements,start,end)
        quicksort(placements,middle+1,end)
        quicksort(placements,start,middle-1)
def partition(placements,start,end):
    pivot=placements[end]
    left_half=start
    right_half=start
    while right_half<=end:
        if placements[right_half]<pivot:
            stuff=placements[left_half]
            placements[left_half]= placements[right_half]
            placements[right_half]=stuff
            left_half=left_half+1
            right_half=right_half+1
        else:
            right_half=right_half+1
    stuff=placements[left_half]
    placements[left_half]= placements[end]
    placements[end]=stuff
    return left_half
storage=[]
print("How long should the list be?")
long=int(input())
for a in range(long):
    print("What number should be in the list?")
    number=int(input())
    storage.append(number)
quicksort(storage,0,long-1)
print(storage)