username="admin"
password="1234"

def login():
    uname=input("Username: ")
    pwd=input("Password: ")
    if uname==username and pwd==password:
        print("\tLogin Successfull!!!")
        return True
    else:
        print("\tInvalid Credentials!")
books={}
def add_books():
    import random
    BookID=random.randint(10000,99999)
    if BookID in books:
        print("\tBookID already exists!")
    else:
        print("Generated Book ID: ",BookID)
        Name=input("Enter Book Name: ")
        Author=input("Enter Author name: ")
        Category=input("Enter the book category: ")
        Price=input("Enter the price of each book: ")
        Total_Copies=input("Enter the total copies present: ")
        books[BookID]={"BookID: ":BookID,"Name: ":Name,"Author: ":Author,"Category: ":Category,"Price: ":Price,"Total_Copies: ":Total_Copies}
        print("\tBook Entered Successfully!")


def update_books(): 
    try:
        BookID=int(input("Enter the BookID of the book whose details you want to update: "))
    except ValueError:
        print("Invalid member ID. Must be a number.")
        return
    if BookID in books:
        Name=input(f"Update Name: [{books[BookID]['Name: ']}]") or books[BookID]['Name: ']
        Author=input(f"Update Author's Nmae: [{books[BookID]['Author: ']}]") or books[BookID]['Author: ']
        Category=input(f"Update Category: [{books[BookID]['Category: ']}]") or books[BookID]['Category: ']
        Price=input(f"Update Price: [{books[BookID]['Price: ']}]") or books[BookID]['Price: ']
        Total_Copies=input(f"Update Total_Copies: [{books[BookID]['Total_Copies: ']}]") or books[BookID]['Total_Copies: ']
        books[BookID]={"BookID: ":BookID,"Name: ":Name,"Author: ":Author,"Category: ":Category,"Price: ":Price,"Total_Copies: ":Total_Copies}
        print("\tBooks updated Successfully!!!")
    else:
        print("\tNo Book with that ID exists!!!")

def delete_books():
    try:
        BookID=int(input("Enter the BookId of the book you want to delete: "))
    except ValueError:
        print("Invalid member ID. Must be a number.")
        return
    if BookID in books:
        del books[BookID]
        print("\tData Deleted Successfully!")
    else:
        print("\tNo book that belongs to this ID exists in this Database!")

def view_all_books():
    if not books:
        print("\tNo books in the library!!!")
    else:
        for BookID, info in books.items():
            print(f"\n{BookID}. ,{info['Name: ']}")
            print(f"    Author's Name: ,{info['Author: ']}")
            print(f"    Category: {info['Category: ']}")
            print(f"    Price: {info['Price: ']}")
            print(f"    Total_Copies: {info['Total_Copies: ']}")

def search_books():
    try:
        BookID=int(input("Enter the BookId of the book you want to search for: "))
    except ValueError:
        print("Invalid member ID. Must be a number.")
        return
    if BookID in books:
        print("Book Found!")
        print("\nBookId: ",BookID)
        print("\nName: ",books[BookID]['Name: '])
        print("\nAuthor Of the Book: ",books[BookID]['Author: '])
        print("\nCategory: ",books[BookID]['Category: '])
        print("\nPrice: ",books[BookID]['Price: '])
        print("\nNumber Of Copies: ",books[BookID]['Total_Copies: '])
    else:
        print("Book not Found!")
members={}
def add_members():
    import random
    member_id=random.randint(1000,9999)
    if member_id in members:
        print("ID already exists in the database.")
    else:
        print("Generated Member ID: ",member_id)
        member_name=input("Enter member name: ")
        mobile_no=input("Enter mobile no: ")
        email_id=input("Enter email id: ")
        borrowed=[]
        members[member_id]={"Member Id: ":member_id,"Member name: ":member_name,"mobile No: ":mobile_no,"email id: ":email_id,"borrowed: ":borrowed}
        print("Member added successfully!!!")
        
def view_members():
    if not members:
        print("\tNo Members in the library!!!")
    else:
        for member_id, info in members.items():
            print(f"\n{member_id}. ,{info['Member name: ']}")
            print(f"    mobile No: ,{info['mobile No: ']}")
            print(f"    email id: {info['email id: ']}")
            print(f"    borrowed: {info['borrowed: ']}")

def borrow_book():
    try:
        member_id = int(input("Enter the Borrower's ID: "))
    except ValueError:
        print("Invalid member ID. Must be a number.")
        return
    try:
        BookID=int(input("Enter the borrowed book ID: "))
    except ValueError:
        print("Invalid member ID. Must be a number.")
        return
    if member_id in members and BookID in books:
        members[member_id]['borrowed: '].append(BookID)
        print(f"[{books[BookID]['Name: ']}] is borrowed by [{members[member_id]['Member name: ']}]")

        print("\nBook successfully borrowed!")
    else:
        print("\tError. Please Try again!")

def return_book():
    try:
        member_id = int(input("Enter the Borrower's ID: "))
    except ValueError:
        print("Invalid member ID. Must be a number.")
        return
    try:
        BookID=int(input("Enter the borrowed book ID: "))
    except ValueError:
        print("Invalid member ID. Must be a number.")
        return
    if member_id in members and BookID in books:
        if BookID in members[member_id]['borrowed: ']:
            members[member_id]['borrowed: '].remove(BookID)
            print(f"[{books[BookID]['Name: ']}] is borrowed by [{members[member_id]['Member name: ']}]")
            print("\nBook successfully returned!")
        else:
            print("\tThis member havent borrowed this book!")
            return
    else:
        print("\tInvalid Credentials!")
        return

def view_borrowed_books():
    try:
        member_id = int(input("Enter the Borrower's ID: "))
    except ValueError:
        print("Invalid member ID. Must be a number.")
        return
    if member_id not in members:
        print("Member not found.")
        return
    elif not members[member_id]['borrowed: ']:
        print("\tNo books borrowed from the library!!!")
        return
    else:
        for BookID in members[member_id]['borrowed: ']:
            print(f"[{books[int(BookID)]['Name: ']}]")



def menu():
    while True:
        print("\n1. Add book")
        print("2. View all books")
        print("3. update book")
        print("4. delete book")
        print("5. view specific book")
        print("6.Add new member")
        print("7.View all members")
        print("8.Borrow a book")
        print("9.return books")
        print("10.view borrowed books")
        print("11. exit")

        choice=input("Enter your Choice")
        if choice=="1":
            add_books()
        elif choice=="2":
            view_all_books()
        elif choice=="3":
            update_books()
        elif choice=="4": 
            delete_books()
        elif choice=="5": 
            search_books()
        elif choice=="6": 
            add_members()
        elif choice=="7": 
            view_members()
        elif choice=="8": 
            borrow_book()
        elif choice=="9": 
            return_book()
        elif choice=="10": 
            view_borrowed_books()
        elif choice=="11":
            print("\tExiting the system...")
            break
        else:
            print("\tInvalid Choice. Please Try again.")

if login():
    menu()