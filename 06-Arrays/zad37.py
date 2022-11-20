li=[[7,3,7,9,0],
    [2,9,0,1,5],
    [3,8,6,4,7],
    [8,7,1,1,5]]

x=int(len(li))
suma=0
for i in range(0,x):
    suma=suma+li[i][-1]

print(suma)
