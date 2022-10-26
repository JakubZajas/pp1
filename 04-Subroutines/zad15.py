from pickle import FALSE, TRUE
from mymath import *

random=generate_number()
print(random)

while TRUE:
 type=read_number()
 if type==random:
    print("Wygrałeś")
    break
 else:
    print("nie")
