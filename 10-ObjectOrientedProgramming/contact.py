class Contact:
    def __init__(self,Name,Email,Phone):
        self.name=str(Name)
        self.email=str(Email)
        self.phone=str(Phone)
        self.kontakt=self.name+"  "+self.email+"  "+self.phone

    def display(self):
        print(self.kontakt)
