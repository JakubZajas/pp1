file = open('numbers.txt','r')
numbers = file.readlines()
suma=0

for i in numbers:
    i=int(i)
    suma=suma+i
    print(i)

print("suma",str(suma))
file.close()