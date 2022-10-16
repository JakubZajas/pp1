from ast import Break
from turtle import done


x=0
suma=0.0
while  True:
    liczba=input("Enter Data:")
    if liczba == 'done':
        break
    try :
        x1=float(liczba)
    except:
        print("Invalid data")
        continue
    x=x+1
    suma=suma+x1
print("DONE")
print("SUMA:", suma)
print("Średnia: ",x1)
print('Liczba liczb:', x)
