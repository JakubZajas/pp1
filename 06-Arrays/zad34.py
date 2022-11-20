def check(ar1,ar2):
    x=int(len(ar1))
    wynik=0
    for i in range(0,x):
        if ar1[i] in ar2:
            wynik=wynik+1
    if wynik==int(len(ar1)):
        print("first array is subset of the second one")

check([1,2,3,4],[1,2,3,4,5,6,7,8,9])