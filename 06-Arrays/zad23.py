def bubblesort(array):
    x=int(len(array))
    swapped=False
    for ch in range(0,x-1):
        for i in range(0,x-1):
            if array[i]>array[i+1]:
                swapped=True
                array[i], array[i + 1] = array[i + 1], array[i]
        if not swapped:
                return
    print(array)


bubblesort([10,12,5,123,7])
bubblesort([64, 34, 25, 12, 22, 11, 90])
bubblesort([9,8,7,6,5,4,3,2,1])