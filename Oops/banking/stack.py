SIZE = 10
class Book:
    def __init__(self, title , author):
        self.title = title
        self.author= author

class shelf:
    def __init__(self):
        self.top =-1
        self.books=[None]*SIZE
    
    def push(self, book):
        if self.top < SIZE:
            self.top += 1
            self.books[self.top]=book
        else:
            print("stack is full ")
    def pop(self):
        if self.top== -1 :
            print("stack is empty ")
        else :
            book = self.books[self.top]
            self.top -= 1
            return book
    def display(self):
        if self.top== -1 :
            print("stack is empty ") 
        else :
            for i in range (self.top , -1 , -1 ):
                print(f"title :{self.books[i].title}, author : {self.books[i].author}")

def main():
    theshelf= shelf()
    while True:
        print("***** Menu *****")
        print("1.add book to shelf")
        print("2.remove book from shelf ")
        print("3.display books ")
        print("4.Exit")

        choice= int(input("enter your choice :  "))

        if choice == 1 :
            title = input("enter title of the book ")
            author= input("enter author of the book ")
            book= Book(title, author)
            theshelf.push(book)

        elif choice== 2:
            theshelf.pop()
        elif choice==3 : 
            theshelf.display()
        elif choice == 4 :
            exit()
        else : 
            print("invalid choice ")

main()