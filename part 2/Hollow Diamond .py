'''
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
'''
print2stars=False
print("The Size Of The Hollow Diamond?")
Size=int(input())
Space=(Size-1)
stars=1
for i in range(Size):
    for o in range(Space):
        print(end=" ")
    print(end="*")
    for e in range(stars-2):
        print(" ",end="")
        print2stars=True
    if print2stars==True:
        print2stars=False
        print("*")
    elif print2stars==False:
        print(" ")
    Space=Space-1
    stars=stars+2
Space=(Space+2)
stars=(stars-4)
for i in range(Size-1):
    for o in range(Space):
        print(end=" ")
    print(end="*")
    for e in range(stars-2):
        print(" ",end="")
        print2stars=True
    if print2stars==True:
        print2stars=False
        print("*")
    elif print2stars==False:
        print(" ")
    Space=Space+1
    stars=stars-2