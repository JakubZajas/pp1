x=int(input("Enter x coordinate:"))
y=int(input("Enter y coordinate:"))
if x>0 and y>0:
    print("Point P(",x,",",y,") is in the first quadrant of the coordinate system")
elif x>0 and y<0:
    print("Point P(",x,",",y,") is in the fourth quaddrant of the coordinate system")
elif x<0 and y>0:
    print("Point P(",x,",",y,") is in the second quadrant of the coordinate system")
elif x<0 and y<0:
    print("Point P(",x,",",y,") is in the third quadrant of the coordinate system")
elif x==0 and y!=0:
    print("Point P(",x,",",y,") is on the OY axis")
elif x!=0 and y==0:
    print("PointP(",x,",",y,") is on the OX axis")
else:
    print("Point P is the beginning of the coordinate system")