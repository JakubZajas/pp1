from pickle import TRUE


suma=0.0
x=0
while TRUE:
 liczba=input("Podaj liczbe: ")
 if liczba == 'done':
          break
 try:
        x1=float(liczba)    
 except:
    print("Invalid data")
    continue
 x=x+1
 suma=suma+x1 
print("All Done")
print("Suma: ", suma)
print("Średnia:", x1)
print("Liczba liczb:",x)