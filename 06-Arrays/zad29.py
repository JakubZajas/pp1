li=[1,10,20,30,40,50,60,70,80,90,100]
number=int(input("enter real number:"))
x=int(len(li))
suma=0
for i in range(0,x):
    if number<li[i]:
        suma=suma+1
print("number of elements that are greater than: ",suma)
