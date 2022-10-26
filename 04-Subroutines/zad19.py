from pickle import TRUE


def fun(n):
    x=int(input("Enter x: "))
    y=int(input("Enter y: "))
    print(bool(n>=x and n<=y))
       
fun(5)