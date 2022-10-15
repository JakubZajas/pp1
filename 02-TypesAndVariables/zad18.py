from cmath import sqrt


a=input('Pierwszy bok:')
b=input("Drugi Bok:")
c=input("Trzeci Bok:")
aa=int(a)
bb=int(b)
cc=int(c)
pp=(aa+bb+cc)/2
P=((pp*(pp-aa)*(pp-bb)*(pp-cc)))**(1/2)
print("Pole trójkąta wynosi:",P)