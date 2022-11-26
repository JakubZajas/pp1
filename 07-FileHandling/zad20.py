from random import randrange
with open("integers_2.txt","w",encoding="utf-8") as integers:
    for i in range(1,51):
        x=randrange(100,999)
        integers.write(str(x))
        integers.write("\n")
integers.close()