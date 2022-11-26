with open("shoppinglist.txt","w",encoding="utf-8") as shoppinglist:
    plik=open('MeatAndFish.txt',"r",encoding="utf-8")
    plikk=open('GrainsAndBread.txt',"r",encoding="utf-8")
    for i in plik:
        shoppinglist.write(i)    
    shoppinglist.write("\n")
    for line in plikk:
        shoppinglist.write(line)   

plikk.close()
plik.close()
shoppinglist.close()