import json

x=input("your name:")
y=input("your surname:")
z=int(input("your age:"))
date=input("your date of birth:")
health=bool(input("do you have health problems? "))
hobby=[]
while True:
    data=input("your hobby: ")
    if data=="":
        break
    else:
        hobby.append(data)

print("\n")
student={
    "name":x,
    "surname":y,
    "age":z,
    "date_of_birth":date,
    "has_health_issues":health,
    "hobby":hobby
}

with open("student.json","w") as file:
    json.dump(student,file,indent=2)

file.close()