def convert(ar):
    x=int(len(ar))
    y=int(len(ar[0]))
    li=[]
    for i in range(0,x):
        for j in range(0,y):
            li.append(ar[i][j])
    
    print(li)


convert([[2,3],
         [1,5]])
convert([[5,0,3,7,5],
         [9,0,9,1,2]])
convert([[2,1],
         [3,5],
         [7,4],
         [2,6]])
    