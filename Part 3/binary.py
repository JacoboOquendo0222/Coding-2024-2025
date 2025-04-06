def binary(key,pattern,end,start):
    if start>end:
        return -1
    middle=int((start+end)/2)
    if pattern[middle]==key:
        return middle
    if pattern[middle]>key:
        return binary(key,pattern,middle-1,start)
    if pattern[middle]<key:
        return binary(key,pattern,end,middle+1)
cage=[1,2,4,9,32,35,92,132,234,521]
print(binary(52188,cage,len(cage),0))