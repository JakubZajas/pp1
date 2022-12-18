from contact import Contact
from contact_list import Contact_List

c1=Contact("John Brown","brown@onet.pl",555234000)
c2=Contact("Anna May","am@o2.pl",232000199)
c3=Contact("George Small","smallg@google.pl",222999100)
c4=Contact("Paola Big","bigpaola@poczta.pl",100200300)

con=Contact_List()
con.new_contact(c1)
con.new_contact(c2)
con.new_contact(c3)
con.new_contact(c4)
con.display()