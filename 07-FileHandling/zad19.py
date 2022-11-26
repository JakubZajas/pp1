with open("integers.txt","w",encoding="utf-8") as integers:
    for i in range(1,51):
        integers.write(str(i))
        integers.write("\n")
integers.close()