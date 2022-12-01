stack=[]
lista=[]
value=input("Enter RPN expresion: ")
for i in value:
    lista.append(i)
for j in lista:
    try:
        j=int(j)
        stack.append(j)
    except:
        if j=="+":
            x=int(stack.pop())
            y=int(stack.pop())
            result=x+y
            stack.append(result)
        elif j=="-":
            x=int(stack.pop())
            y=int(stack.pop())
            result=x-y
            stack.append(result)
        elif j=="*":
            x=int(stack.pop())
            y=int(stack.pop())
            result=x*y
            stack.append(result)
        elif j=="/":
            x=int(stack.pop())
            y=int(stack.pop())
            result=x/y
            stack.append(result)
        elif j=="=":
            print(stack.pop())