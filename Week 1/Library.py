#----LIBRARY PROGRAM----
# This program manages a library inventory 
# that allows users to borrow and return books from the library.

class Library:
    
    #constructor
    def __init__(self, books):
        self.books = books   #stores the list of books              

    #method
    def borrow_book(self, book):
        if book in self.books:  #checks if asked book is available or not
            self.books.remove(book)
            print("\nBorrowed!")
        else:
            print("\nNot available.")
        print(f"Updated List: {self.books}") #shows list after borrowing

    #method
    def return_book(self, book):
        self.books.append(book)              #adds a book to the library list
        print("\nReturned!")
        print(f"Updated List: {self.books}") #shows list after returning

#create library list of books (object)
lib = Library(["Python", "Java", "C++", "Math", "Physics", "English"])

print(f"\nBook List: {lib.books}")

while True:
    choice = input("\nChoose --> 1:Borrow, 2:Return, 3:Exit ")

    if choice == "1":
        lib.borrow_book(input("Enter book name: "))
    elif choice == "2":
        lib.return_book(input("Enter book name: "))
    elif choice == "3":
        break     #stops
