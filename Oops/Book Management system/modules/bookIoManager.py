import csv 
from modules import books
from modules import bookrepository
class BookManager :

    def __init__(self, filename="books.csv"):
        self.filename =filename

    def add_book(self, bookId, bookname, author, price, quantity):
        with open (self.filename, "w",newline=" ")as f:
            writer = csv.writer(f)
            #writer.writerow(["id", "title" , "author", "price" , "quantity"])
            for book in self.repository.getAll():
                writer.writerow([book.BookId, book.Bookname, book.author, book.price, book.quantity])
                
    def loadBooks(self):
        books = []
        with open (self.filename, "r") as f:
            reader = csv.reader(f)
            next(reader) # Skip header row
            for row in reader:
                bookId, bookname, author, price, quantity = row
                book = books(bookId, bookname, author, float(price), int(quantity))
                books.append(book)
        return books

    def load_from_file(self):
        try:
            with open(self.filename, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.manager.add_book(int(row["id"]), row["title"], row["author"], float(row["price"]))
        except FileNotFoundError:
            pass  # Ignore if file does not exis