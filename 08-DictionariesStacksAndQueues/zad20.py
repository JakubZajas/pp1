number=int(input("Natural number: "))
stack=[]

while number != 0:
    x=number%2
    stack.append(x)
    number=number//2

print("Binary number: ",end="")
for i in range(len(stack)):
        print(stack.pop(),end="")