import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
x=0
for i in range(0,len(temperatures)):
    x=x+int(temperatures[i])

wynik=x/len(temperatures)
print(wynik)