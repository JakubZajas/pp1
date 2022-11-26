import csv
with open("students.csv","r",encoding="utf-8",newline='') as students:
    reader=csv.reader(students)  
    header=next(reader)
    x=0
    data=[]
    for row in reader:
        first_name=str(row[0])
        last_name=str(row[1])
        age=int(row[2])
        gender=str(row[3])
        email=str(row[4])
        data.append([first_name,last_name,age,gender,email])
    
    for i in range(5):
        x=x+1

    for j in range(x):
        if data[j][2]<30:
            name=data[j][0]
            lastname=data[j][1]
            mail=data[j][4]

            print(name,end="    ") 
            print(lastname,end="   ")
            print(mail)
            
        
    students.close()