x=input("File name: ")
suma=0

with open(x,"r") as plik:
    for line in plik:
        suma=suma+1

print("Number of lines: ",suma)
plik.close()
