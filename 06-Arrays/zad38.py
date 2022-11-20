def create_2d_arr(x,y):
    li=[]
    for dd in range(0,y):
        li.append([])
    for i in range(0,x):
        for ch in range(0,y):
            li[ch].insert(i,0)
    print(li)
        
create_2d_arr(3,5)
create_2d_arr(4,7)