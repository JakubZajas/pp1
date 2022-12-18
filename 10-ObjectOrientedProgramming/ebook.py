class E_book:
    def __init__(self,Title,Autor,Pages,):
        self.title=Title
        self.autor=Autor
        self.pages=Pages
        self.current_page=False

    def open(self,Current_Page):
        self.current_page=Current_Page
    
    def close(self):
        self.current_page=False

    def next(self):
        if self.current_page:
            self.current_page=self.current_page+1
    
    def previous(self):
        if self.current_page:
            self.current_page=self.current_page-1

    def status(self):
        if self.current_page:
            print("aktualna strona:" ,+self.current_page)
        else:
            print("Książka jest zamknięta")   
    def inf(self):
        print(self.title,self.autor,self.pages)