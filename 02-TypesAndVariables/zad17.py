x=input("Podaj wzrost w cm:")
xx=int(x)
y=(xx//30.48)
z=(xx%2.54)
print("I am",(xx),'cm tall, i.e.',round(y,2) ,'feet and',round(z,2),'inches')