def f(player1,player2):
    l1=[]
    l2=[]
    sum1=0
    sum2=0
    for i in player1:
        l1.append(i)
    for j in player2:
        l2.append(j)
    for value in l1:
        try:
            value=int(value)
            sum1=sum1+value
        except:
            if value=="A":
                sum1=sum1+10
            elif value=="K":
                sum1=sum1+10
            elif value=="Q":
                sum1=sum1+10
            elif value=="J":
                sum1=sum1+10
            elif value=="T":
                sum1=sum1+10
    for value in l2:
        try:
            value=int(value)
            sum2=sum2+value
        except:
            if value=="A":
                sum2=sum2+10
            elif value=="K":
                sum2=sum2+10
            elif value=="Q":
                sum2=sum2+10
            elif value=="J":
                sum2=sum2+10
            elif value=="T":
                sum2=sum2+10

    print(bool(sum1>sum2))
    return bool(sum1>sum2)
    
f("AJ972","AQT72") 
f("9532","K8") 
f("987","AT4") 
f("V1VV","10")