class Book:
    def __init__(self, title, year_of_release,character):
        self.title=title
        self.year_of_release=year_of_release
        self.character=character

    def myfunc(self):
        print("Title is " + self.title)
        print("Year of Relese is " + self.year_of_release)
        print("Main character is "+ self.character)

p1 = Book("Hobbit","1937","Bilbo")
p1.myfunc()

