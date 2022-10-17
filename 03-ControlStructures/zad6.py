try:
 speed=int(input("Enter car speed in km/h:"))
 if speed>130 and speed!=0 and speed>0:
    print("Exceeds the speed limit")
 elif speed<=130  and speed>=0:
    print("Does not exceed the speed limit.")
 else:
    print("Wrong data.")
except:
    print("Wrong Data")