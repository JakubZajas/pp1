class Student:
    university="UEK Kraków"
    album=100000     

    def __init__(self,Name,Surname,Field):
        self.name=Name
        self.surname=Surname
        self.field=Field
        self.id=Student.album
        Student.album+=1

    def __str__(self):
        return f"{ self.name} {(self.surname).upper()} ({self.id}), {self.field}, {Student.university}"

    
s1=Student("Anna","MAj","AI")
s2=Student("Jan","Kowalski","Mathematic")
s3=Student("Kacper","Satyra","Philosphy")
print(s1)
print(s2)
print(s3)