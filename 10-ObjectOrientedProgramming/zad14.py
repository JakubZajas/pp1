from ebook import E_book


ebook1=E_book("Hobbit","Tolkien",500)
ebook1.inf()
ebook1.open(1)
ebook1.status()
ebook1.next()
ebook1.next()
ebook1.next()
ebook1.next()
ebook1.status()
ebook1.close()
ebook1.next()
ebook1.next()
ebook1.status()

ebook1=E_book("Igrzyska Śmierci","Nieważne",700)
ebook1.inf()
ebook1.open(125)
ebook1.status()
ebook1.next()
ebook1.next()
ebook1.next()
ebook1.next()
ebook1.status()
ebook1.close()
ebook1.next()
ebook1.next()
ebook1.status()