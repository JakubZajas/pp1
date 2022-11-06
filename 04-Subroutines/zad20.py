def power (x,n):
    if n>=1:
        return x*power(x,n-1)
    else:
        return 1
print(power(2,3))