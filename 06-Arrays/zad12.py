li=[[2,5,4],
    [9,0,3]]
#a
print(li)
#b
print(len(li), end="  ")
print(len(li[0]))
#c
print(li[0][1])
#d
print(li[1][2])
#e
print(li[1][0],li[1][1],li[1][2])
#f
print(li[0][0],li[0][1],li[0][2])
print(li[1][0],li[1][1],li[1][2])

#ostatnia kolumna gdy nie znamy wielkości wielkości x i y
for i in range(0,len(li)):
    print(li[i][len(li)])