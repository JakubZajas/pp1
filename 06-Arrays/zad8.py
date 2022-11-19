li=[-15,8,-31,47,-2,19]

def a():
    najw=li[0]
    najm=li[0]
    for i in range(0,len(li)-1):
        if li[i]>li[i+1]:
            najw=li[i]
    print(najw)
    for x in range(0,len(li)-1):
        if li[x]<li[x+1]:
            if li[x]<najm:
                najm=li[x]
    print(najm)

a()