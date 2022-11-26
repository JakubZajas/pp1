import re
mess="To be, or not to be, that is the question"
a=re.findall("a",mess)
e=re.findall("e",mess)
i=re.findall("b",mess)
o=re.findall("o",mess)
y=re.findall("y",mess)
suma=a+e+i+o+y
print(len(suma))