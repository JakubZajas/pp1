with open("original.txt","r",encoding="utf-8") as original:
    plik=open('copy.txt',"w",encoding="utf-8")
    for line in original:
        plik.write(line)


plik.close()
original.close()