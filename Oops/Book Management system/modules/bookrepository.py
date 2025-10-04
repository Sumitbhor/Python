from modules import books
from modules import bookIoManager
class bookrepository:
    def insert(self,book):
        print("Book is added ")

    def getAll(self):
        print("These all are books avialble in library")

    def update (self, bookId, updateBook):
        print("existing book is updated") 
        
    def delete(self, BookId):
        print("Book is removed from libary")
    