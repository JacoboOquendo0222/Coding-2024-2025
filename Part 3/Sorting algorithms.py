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
storage=[]
print("How long should the list be?")
long=int(input())
for a in range(long):
    print("What number should be in the list?")
    number=int(input())
    storage.append(number)
merge(storage,0,long-1)
print(storage)