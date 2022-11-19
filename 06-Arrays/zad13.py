li=[[3,9,2],
    [2,4,5],
    [7,1,6],
    [0,4,8]]
suma=0
x=int(len(li))
y=int(len(li[0]))
for i in range(0,x):
    for ch in range(0,y):
        if li[i][ch]%2==0:
            suma=suma+li[i][ch]

print(suma)

