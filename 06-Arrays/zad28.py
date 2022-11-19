def mediana(li):
    x=int(len(li))
    y=int(x//2)
    if li[y]%2!=0:
        print(li[y])
    else:
        suma=(li[y]+li[y-1])/2
        print(suma)

mediana([1,0,9,4,6])
mediana([6,8,3,1,0,5,7])
mediana([1,2,3,4,5,6])