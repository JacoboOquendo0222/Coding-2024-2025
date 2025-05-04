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
def merge(placements):
    for ei in range(0,len(placements))                
storage=[]
print("How long should the list be?")
long=int(input())
for a in range(long):
    print("What number should be in the list?")
    number=int(input())
    storage.append(number)
bubble_sort(storage)
print(storage)