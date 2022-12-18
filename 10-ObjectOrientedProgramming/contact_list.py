
class Contact_List:
    from contact import Contact
    def __init__(self):
            self.contacts=[]
        

    def new_contact(self,kon):
        self.kon=kon
        self.contacts.append(self.kon)

    def display(self):
        print(self.contacts)
    
    def __str__(self):
        print(self.contacts)


from contact import Contact
c4=Contact("Paola Big","bigpaola@poczta.pl",100200300)
con=Contact_List()
con.new_contact(c4)
con.__str__()