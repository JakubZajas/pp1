import re
mess="To be, or not to be, that is the question"
pattern=r"[aeiouy]"
suma=re.findall(pattern,mess)
print(len(suma))