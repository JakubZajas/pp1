from pickle import FALSE, TRUE
from mymath import *

guess=generate_number()
print(guess)

wrong=TRUE

while wrong:
    x=read_number()
    if guess==x:
        wrong= FALSE
print("Wygrałeś")
