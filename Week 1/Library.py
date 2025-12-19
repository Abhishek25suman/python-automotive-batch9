class Library:
    
    def __init__(self, books):
        self.books = books

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Borrowed!")
        else:
            print("\nNot available.")
        print(f"Updated List: {self.books}") #Shows list after borrowing

    def return_book(self, book):
        self.books.append(book)
        print("\nReturned!")
        print(f"Updated List: {self.books}") #Shows list after returning

lib = Library(["Python", "Java", "C++", "Math", "Physics", "English"])

print(f"Book List: {lib.books}")

while True:
    choice = input("Choose --> 1:Borrow, 2:Return, 3:Exit ")

    if choice == "1":
        lib.borrow_book(input("Enter book name: "))
    elif choice == "2":
        lib.return_book(input("Enter book name: "))
    elif choice == "3":
        break