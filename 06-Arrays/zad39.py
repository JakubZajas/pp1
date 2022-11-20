li=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
x=int(len(li))
y=int(len(li[0]))
for i in range(0,x):
    li[0][i]=i+1
    li[i][0]=i+1
for i in range(0,x):
    for ch in range(0,y):
        li[i][ch]=li[0][i]*li[ch][0]




print(li)