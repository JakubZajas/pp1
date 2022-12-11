def f(array2D):
    li=[]
    
    for i in range(len(array2D[0])):
        sum=0
        for j in range(len(array2D)):
            sum=sum+array2D[j][i]
        li.append(sum)
           
            

    

    print(li)
    return li



f([ [3,6,2,7], [9,5,4,0], [2,8,0,9] ]) 
f([ [3,6,2], [9,5,4], [2,8,0] ]) 
f([ [3,6], [9,5], [2,8] ]) 
f([ [3,6,3,1], [9,3,4,0], [2,1,0,10] ]) 