li1=[4,36,12,28,9,44,5] 
li2=[5,1,36]


x=int(len(li2))
for i in range(0,x):
    if li2[i] in li1:
        li1.remove(li2[i])

print(li1)


