import re
filename='grades.txt'
code="\w.[0-6]"   
suma=0
lista=[]
with open(filename,"r") as file:
    new_file=file.read()
    for line in new_file:
        plik=re.split(":",new_file)
        
    actual_file=re.split(",",plik[2])
    for j in actual_file:
        lista.append(float(j))

    for i in lista:
        i=float(i)
        suma=suma+i
    
    leng=len(actual_file)
    avg=suma//leng
    print(avg)