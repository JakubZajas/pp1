li=[[1,2],
    [3,4],
    [5,6],
    [7,8]]

x=int(len(li))
y=int(len(li[0]))

for i in range(0,x):
    for ch in range(0,y):
        print(li[i][ch],end="")
    print('\n')

for ch in range(0,y):
    if ch>0:
        print("\n")
    for i in range(0,x):
        print(li[i][ch],end="")