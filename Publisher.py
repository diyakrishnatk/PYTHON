class Publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"name :{self.name}")
class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author
    def display(self):
        super().display()
        print(f"title :{self.title}")
        print(f"author :{self.author}")
class Python(Book):
    def __init__(self,name ,title,author,price,page_no):
        super().__init__(name,title,author)
        self.price=price
        self.page_no=page_no
    def display(self):
        super().display()
        print(f"price : {self.price}")
        print(f"page no : {self.page_no}")
Book1=Python("dc","adduuujee","basheer",200,300)
Book1.display()