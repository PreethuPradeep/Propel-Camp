books={}
username="admin"
password="1234"
def login():
    uname=input("Enter the username: ")
    pwd=input("Enter the password")
    if uname==username and pwd==password:
        print("Login Successful!")
        return True
    else:
        print("Invalid Credentials!")
        return False

def add_books():
    BookId=input("Enter the BookId")
    if BookId in books:
        print("There already exists a book under this Id. Try again.")
        return
    Title=input("Enter the book title")
    Author=input("Enter the name of the Author")
    Year=input("Enter the year of publishing")
    NumCopies=input("Enter the number of copies")
    books[BookId]={"Title: ":Title,"Author Of the Book: ":Author,"Year Of Publishing: ":Year,"Number Of Copies: ":NumCopies}
    print("This book is added to the Library. Thank You for your Contribution.")

def View_all_books():
    if not books:
        print("No books were found in the libarary!")
    else:
        for BookId, info in books.items():
            print(f"{BookId}. ,{info['Title: ']},\n    Author's Name: {info['Author Of the Book: ']},\n    Year Of Publishing: {info['Year Of Publishing: ']},\n    Number of Copies: {info['Number Of Copies: ']}")

def update_books():
    BookId=input("Enter the Book Id of the book you want to update: ")
    if BookId in books:
        print("Enter new Details... or leave empty if you want to keep the current value")
        Title=input(f"Update Title: [{books[BookId]['Title: ']}]") or books[BookId]['Title: ']
        Author=input(f"\nUpdate Author's Name: [{books[BookId]['Author Of the Book: ']}]") or books[BookId]['Author Of the Book: ']
        Year=input(f"\nYear Of Publishing: [{books[BookId]['Year Of Publishing: ']}]") or books[BookId]['Year Of Publishing: ']
        NumCopies=input(f"\nNumber of Copies: [{books[BookId]['Number Of Copies: ']}]") or books[BookId]['Number Of Copies: ']
        books[BookId]={"Title: ":Title,"Author Of the Book: ":Author,"Year Of Publishing: ":Year,"Number Of Copies: ":NumCopies}

def delete_book():
    BookId=input("Enter the BookId of the book you want to remove: ")
    if BookId in books:
        del books[BookId]
        print("Book details deleted from the system.")
    else:
        print("No such Book in the system. Try Again.")

def search_book():
    BookId=input("Enter the BookId of the book you want to search for: ")
    if BookId in books:
        print("Book Found!")
        print("\nBookId: ",BookId)
        print("\nTitle: ",books[BookId]['Title: '])
        print("\nAuthor Of the Book: ",books[BookId]['Author Of the Book: '])
        print("\nYear Of Publishing: ",books[BookId]['Year Of Publishing: '])
        print("\nNumber Of Copies: ",books[BookId]['Number Of Copies: '])
    else:
        print("Book not Found!")
              

def menu():
    while True:
        print("\n1. Add book")
        print("2. View all books")
        print("3. update book")
        print("4. delete book")
        print("5. search book")
        print("6. exit")

        choice=input("Enter your Choice")
        if choice=="1":
            add_books()
        elif choice=="2":
            View_all_books()
        elif choice=="3":
            update_books()
        elif choice=="4": 
            delete_book()
        elif choice=="5":
            search_book()
        elif choice=="6":
            print("Exiting the system...")
            break
        else:
            print("Invalid Choice. Please Try again.")

if login():
    menu()

