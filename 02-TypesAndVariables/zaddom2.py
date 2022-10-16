try:
 xx=float(input("Please enter a score from 0.0 to 1.0:"))
 x=float(xx)
 if x>=0.9 and x<1:
  print("A")
 elif x>= 0.8 and x<0.9:
  print("B")
 elif x>= 0.7 and x<0.8:
  print("C")
 elif x>= 0.6 and x<0.7: 
  print("D")
 elif x<  0.6:
  print("E")
 elif x>1:
    print("Bad Score")
except:
 print("Bad score")