from random import randrange

def rand_elem(array):
    y=int(len(array))
    x=randrange(0,y)
    print(array[x])

rand_elem([1,2,3,4,5,6,7,8,9])