
def transpose_matrix(m):
    print(m)
    x=int(len(m))
    y=int(len(m[0]))
    result=[]
    for ch in range(0,y):
        result.append([])
    for i in range(0,y):
        for j in range(0,x):
            result[i].append(m[j][i])
    
    for char in range(0,y):
        print(result[char])

transpose_matrix([[1,2,3],[4,5,6],[7,8,9]])
transpose_matrix([[1,2,3,4,5],[6,7,8,9,0]])
transpose_matrix([[5,6,7,8]])



