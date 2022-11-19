def power (x,n):
    while n>=1:
        print(x*power(x,n-1))
        return x*power(x,n-1)
    else:
        return 1 
    


power(2,3)