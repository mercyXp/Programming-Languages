class Book:
    def __init__(self,title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def is_long(self):
        return "True" if self.pages > 300 else "False"

book1 = Book("Animal Farm", "George Orwell", 245)
book2 = Book("Rich Dad Poor Dad", "Richard Kiosk", 358)

print(book1.is_long())
print(book2.is_long())