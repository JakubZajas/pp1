import re
filename='grades.txt'
code="\w.[0-6]"   
plik=[]
suma=0
with open(filename,"r",encoding="utf-8") as file:
    lines=file.readlines()
for line in lines:
    new_file=re.split(":",line,)
list=new_file[1]
new_list=re.split(",",list)
x=int(len(new_list))
for i in range(0,x):
    suma=suma+float(new_list[i])
wynik=int(suma/x)
print(wynik)