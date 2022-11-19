li=[2,3,2,5,8,1,9,8]
x=int(len(li))
lista=[]
for i in range(0,x):
    if li[i] in lista:
        lista.remove(li[i])
    else:
        lista.append(li[i])

print(lista)    