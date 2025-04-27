def insertion_sort(placements):
    for io in range(0,len(placements)):
        finding=io
        for iae in range(io,-0,-1)
def sorting(placements):
    for o in range(0,len(placements)):
        finding=o
        for i in range(o,len(placements)):
            if placements[i]<placements[finding]:
                finding=i
        stuff=placements[o]
        placements[o]=placements[finding]
        placements[finding]=stuff
storage=[]
print("How long should the list be?")
long=int(input())
for a in range(long):
    print("What number should be in the list?")
    number=int(input())
    storage.append(number)
sorting(storage)
print(storage)