with open("30lines.txt","r",encoding="utf-8") as plik: 
    j=0
    p=4
    booll=True
    for i in plik:
        print(i)
        j=j+1
        if j>p:
            p=p+5
            break
    while booll==True:   
        x=input("Press ENTER to print 5 more lines")
        if x=="":
           for i in plik:
            print(i)
            j=j+1
            if j>p:
                p=p+5
                break
            

plik.close()