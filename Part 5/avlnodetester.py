from avlnode import nodeavl
lvanode=nodeavl(0)
leftnode=nodeavl(2)
lvanode.setleft(leftnode)
lvanode.update()
print(lvanode.getmaxheight())
print(lvanode.getbalancefactor())

