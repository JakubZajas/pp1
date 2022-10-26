def letter():
    x="You never get a second chance to make a first impression"
    
    count=0
    for c in x:
        if c=="e":
            count=count+1
    print(count)

letter()