li=[1,2,3,4,5,6,7,8,9]
x=int(len(li))
even=[]
odd=[]
for i in range(0,x):
    if li[i]%2==0:
        even.append(li[i])
    elif li[i]%2!=0:
        odd.append(li[i])

print(even+odd)
