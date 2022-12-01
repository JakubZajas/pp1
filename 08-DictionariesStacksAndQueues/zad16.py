import json
    
with open("students.json","r") as jsoon:
    file=json.load(jsoon)


for i in file:
    for k,v in i.items():
        if k=="name":
            print(k,":",v)
        elif k=="surname":
            print(k,":",v)
        elif k=="student_id":
            print(k,":",v)
    print("\n")


jsoon.close()