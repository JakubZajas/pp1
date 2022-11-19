li=[[True,False],
    [True,True],
    [False,False]]
x=int(len(li))
y=int(len(li[0]))

for i in range(0,x):
    for ch in range(0,y):
        if li[i][ch]== True:
            li[i][ch]= False
        elif li[i][ch]==False:
            li[i][ch]= True

print(li)