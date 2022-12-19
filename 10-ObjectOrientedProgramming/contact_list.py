
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
con=c4.convert()
conn=Contact_List()
conn.new_contact(con)
conn.__str__()


float('3.14')