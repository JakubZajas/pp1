def compare(array1, array2):
    print("array1: ",array1)
    print("array1: ",array2)
    x=int(len(array1))
    suma=0

    try:
        for i in range(0,x):
            if len(array1)!=len(array2):
                break
            if array1[i]!=array2[i]:
                break
            elif array1[i]!=array2[i]:
                break
            else:
               suma=suma+1
    except:
        print("error")

    if suma==len(array1):
        print("Comparison: arrays are the same")
    else:
        print("Comparison: arrays are not the same")



compare([5,3,1],[5,3,1])
compare(["water","book","sky"],["water","book","sky"])
compare([True,False],[True,False,True])
compare([3,2,1],[3,2])