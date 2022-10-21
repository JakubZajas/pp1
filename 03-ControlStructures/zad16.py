try:
 x=int(input("Enter first number:"))
 y=int(input("Enter seconbd number:"))
 if x>y:
    print("Numbers in ascending order:",x,y)
 elif x==y:
    print("Numbers are equal")
 else:
    print("Numbers in ascending order:",y,x)
except:
    print("Wrong Data idiot")