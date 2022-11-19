import array as arr


ar1=arr.array("i",[2,3,7,5,4])

#a
def a():
    print(ar1)

#b
def b():
    print(len(ar1))
#c
def c():
    print(ar1[0])

#d
def d():
    print(ar1[1])

#e
def e():
    print(ar1[-1])

#f
def f():
    print(ar1[-2])

#g
def g():
    print(ar1[0]+ar1[-1])

#h
def h():
    x=int(len(ar1)/2)
    print(ar1[x])

#i
def i():
    for x in range(len(ar1)):
        print(ar1[x],end=" ")

#j
def j():
    x=(len(ar1)//2)+1
    for y in range(x):
        print(ar1[y],end=" ")

j()