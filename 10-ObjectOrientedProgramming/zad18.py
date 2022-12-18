class Contact:
    def __init__(self,Name,Email,Phone):
        self.name=Name
        self.email=Email
        self.phone=Phone
    
    def display(self):
        print(self.name,self.email,self.phone)


c1=Contact("John Brown","brown@onet.pl",555234000)
c1.display()