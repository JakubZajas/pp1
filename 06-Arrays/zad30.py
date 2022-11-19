def minmax(array):
    array.sort()
    lista=[]
    lista.append(array[0])
    lista.append(array[-1])
    print(lista)

minmax([4,2,8,4,7,9,5])