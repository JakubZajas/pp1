import array as arr
import random

#a
arr1 =arr.array("i",[3,7,1,0,4])
print(arr1)

#b
arr2=arr.array("u",str([[2,3],[7,1],[0,4]]))
print(arr2)

#c
arr3=arr.array("i",[7 for i in range(5)])
print(arr3)

#d
arr4 =arr.array("i",[i for i in range(1,10)])
print(arr4)

#e
arr5 =arr.array("i",[i*2 for i in range(1,10)])
print(arr5)

#f
arr6 =arr.array("i",[random.randint(1,20) for i in range(10)])
print(arr6)

#g
arr7 =arr.array("u",str([[] for i in range(5)]))
print(arr7)

#h
arr8 =arr.array("u",str([[1 for i in range(2)] for j in range(4)]))
print(arr8)

#i
arr9 =arr.array("u",str([[random.randint(1,20) for i in range(3)] for j in range(5)]))
print(arr9)

#j
arr10=arr.array("i",[4,0,3])
print(arr10)

#k
arr11=arr.array("i",50*[0])
print(arr11)

#l
arr12=arr.array("i",[i for i in range(1,31)])
print(arr12)

#m
arr13=arr.array("i",[random.randint(0,1) for i in range(1,21)])
print(arr13)

#n
arr14=arr.array("u",str([
    [False,False],
    [False,False],
    [False,False],
    [False,False],
    [False,False]
]))
print(arr14)