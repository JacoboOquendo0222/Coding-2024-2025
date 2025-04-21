def sorting(placements):
    finding=0
    for i in range(0,len(placements)):
        if placements[i]<placements[finding]:
            finding=i
    stuff=placements[0]
    placements[0]=placements[finding]
    placements[finding]=stuff
def selection_sort(placements)
storage=[9,1,4,2,5,7,3,20,34,10,8]
sorting(storage)
print(storage)
