li=[[0,0,0],[0,0,0],[0,0,0]]

x=int(len(li))
y=int(len(li[0]))

for i in range(0,x):
    for i in range(0,y):
        li[i][i]=1

print(li[0][0],li[0][1],li[0][2])
print(li[1][0],li[1][1],li[1][2])
print(li[2][0],li[2][1],li[2][2])
    