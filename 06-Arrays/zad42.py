li=[[1,2,3],
    [4,5,6],
    [7,8,9],
    [1,3,5],
    [2,4,6]]
print(li)
x=int(len(li))

swap=[]
for i in range(0,x):
    swap.append(li[i][-1])

for ch in range(0,x):
    li[ch][-1]=li[ch][0]

for dd in range(0,x):
    li[dd][0]=swap[dd]

print(li)