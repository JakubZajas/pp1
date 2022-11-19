li=[1,2,3,4,5,6,7,8,9,10,11]
x=0
suma=0
odd=0
while x<len(li):    
    if li[x]%2==0:
        suma=suma+li[x]
        x=x+1
    elif li[x]%2!=0:
        odd=odd+li[x]
        x=x+1
print(suma)
print(odd)