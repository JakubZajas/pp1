import re
file = open('refile.txt','r',encoding="utf-8",newline="")
plik=[]
for line in file:
    plik.append(line)
    plik=str(plik)
find=re.findall("\S{6,}",plik)
print(find)

x=int(len(find))

for i in range(0,x):
    print(find[i])

file.close()