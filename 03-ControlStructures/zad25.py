a=int(input("Podaj bok a:"))
b=int(input("Podaj bok b:"))
print("*"*a)
x= " "
for i in range(b-2):
    print("*",x*(a-4),"*")
print("*"*a)