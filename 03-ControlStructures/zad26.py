from tkinter import END
from xml.dom.pulldom import END_DOCUMENT


for x in range(1,4):
     code=str(input("Enter the PIN code: "))
     if code!=str("0805"):
        print("Incorrect...")
     elif code=="0805":
        print("You have logged in")
        break
     if x>=3:
      print("Sorry, your payment card has been blocked.")

    