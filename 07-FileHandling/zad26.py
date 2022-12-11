import re
file = open('refile.txt','r',encoding="utf-8",newline="")
plik=file.read()
pattern=r"\w{6,}"
find=re.findall(pattern,plik)
print(find)

x=int(len(find))

for i in range(0,x):
    print(find[i])
print(len(find))
file.close()