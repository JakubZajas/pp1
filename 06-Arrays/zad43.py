def identity_matrix(n):
    li=[]
    for i in range(0,n):   
        li.append([])
    for ch in  range(0,n): 
        for dd in range(0,n):
            li[ch].append(0)  
    
    for index in range(0,n):
        li[index][index]=1

    for char in range(0,n):
        print(li[char])

identity_matrix(3)
identity_matrix(5)
identity_matrix(8)
