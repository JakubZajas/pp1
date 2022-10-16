try:
    x=int(input("Enter Hours:"))
    yyy=int(input("Enter Rate:"))

    if x>40:
        z=x-40
        yy=yyy*1.5
        p=(z*yy)+400
        print(p)
    else:
        xx=x*yyy
        print(xx)
except:
    print("Error, please enter numeric input")