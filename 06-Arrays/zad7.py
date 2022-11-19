import array as arr


def a():
    ar1=arr.array("i",[1,2,3,4,5])
    ar1[0]=ar1[0]-1
    print(ar1)

def b():
    ar1=arr.array("i",[1,2,3,4,5])
    ar1[-1]=ar1[-1]+4
    print(ar1)

def c():
    ar1=arr.array("i",[1,2,3,4,5])
    x=len(ar1)//2
    ar1[x]=ar1[x]*2
    print(ar1)

def d():
    ar1=arr.array("i",[1,2,3,4,5])
    for x in range(len(ar1)):
        ar1[x]=ar1[x]+3
    print(ar1)


a()
b()
c()
d()
