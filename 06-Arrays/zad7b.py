x=[1,2,3,4,5]

#a
def a():
    x=[1,2,3,4,5]
    x[0]=x[0]-1
    print(x)

def b():
    x=[1,2,3,4,5]
    x[len(x)-1]=x[len(x)-1]+4
    print(x)

def c():
    x=[1,2,3,4,5]
    x[len(x)//2]=x[len(x)//2]*2
    print(x)

def d():
    x=[1,2,3,4,5]
    for y in range(len(x)):
        x[y]=x[y]+3
    print(x)
a()
b()
c()
d()
