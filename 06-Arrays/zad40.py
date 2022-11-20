li=[[-38, 19], [5,40],[-7,11],[29,16]]
x=int(len(li))
y=int(len(li[0]))
najw=li[0][0]
najm=li[0][0]
for i in range(0,x):
    for ch in range(0,y):
        if li[i][ch]>najw:
            najw=li[i][ch]
        elif li[i][ch]<najm:
            najm=li[i][ch]

print(najw)
print(najm)