with open("power.txt","w",encoding="utf-8") as power:
    for i in range(1,11):
        j=i**2
        k=i**3
        j=str(j)
        k=str(k)
        i=str(i)
        power.write(i)
        power.write(",")
        power.write(j)
        power.write(",")
        power.write(k)
        power.write("\n")

power.close()