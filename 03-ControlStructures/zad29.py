from tkinter import END
z=0
y=0
x=1
while x!=0:
    x=int(input("Enter number:"))
    y=y+x
    z=z+1
else:
    END
mean=y/(z-1)
print("RESULT: Quantity:",z-1,"Sum=",y,"Mean=",mean)