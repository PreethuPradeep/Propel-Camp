#Given a list of positive integers of size 'n'. find the second largest number.

list=[32,5,234,154,351,52,6,47,34]
l=len(list)
list.sort()
print(list[l-2])


#given a list, unsorted, find the number of elements larger than k=3
list=[5,8,7,3,12,1,2,0,10,4]
list1=[]
k=3
list2=[]
for i in range(k-1,len(list)):
    a=list[i]
    list1.append(a)
    list1.sort()
a=list[0]
b=list[1]
list2.append(a)
list2.append(b)
list2=list2+list1
print(list2)



#Student management System
#First we need to set the login credentials
#So we are setting a user name and password
username="admin"
password="1234"
#we are creating an empty dictionary students
students={}
#create the login function
def login():
    print("-----Student Mnagement System login------")
    uname=input("username: ")
    pwd=input("Password")
    if uname==username and pwd==password:
        print("Login Successful!\n")
        return True
    else:
        print("Invalid Credentials!\n")
        return False

#fucntion to add student
def add_student():
    roll=input("Enter roll number")
    if roll in students:
        print("Student already exists")
        return
    name=input("Enter name")
    clas=input("enter class")
    phone=input("enter phone number")
    students[roll]={"name: ":name,"class: ":clas,"phone: ":phone}
    print("Student Added successfully!")


#edit student
def edit_student():
    roll=input("Enter roll number to edit")
    if roll in students:
        print("Enter new details...(leave empty to keep current value)")
        name=input(f"New name[{students[roll]['name: ']}]") or students[roll]['name: ']
        clas=input(f"New class[{students[roll]['class: ']}]") or students[roll]['class: ']
        phone=input(f"New phone number[{students[roll]['phone: ']}]") or students[roll]['phone: ']
        students[roll]={"name: ":name,"class: ":clas,"phone no: ":phone}
        print("Student details Updated")
    else:
        print("Student Not Found!")

#delete a student
def del_student():
    roll=input("Enter the roll number to delete")
    if roll in students:
        del students[roll]
        print("Student details Deleted")
    else:
        print("Student Not Found!")

#To search a student
def search_student():
    roll=input("Enter a roll number to search")
    if roll in students:
        print(f"Student deatils Found!")
        print("\nRoll: ",roll)
        print("\nName: ",students[roll]['name: '])
        print("\nClass: ",students[roll]['class: '])
        print("\nPhone: ",students[roll]['phone no: '])
    else:
        print("Student Not Found!")

#To List Students
def list_students():
    if not students:
        print("No students found!")
    else:
        print("Students Found!")
        for roll, info in students.items():
            print(f"Roll: {roll},Name:{info['name: ']},class: {info['class: ']},Phone: {info['phone no: ']}")


def menu():
    while True:
        print("\n1.Add Student")
        print("2.Edit Student")
        print("3.Delete Student")
        print("4.Search Student")
        print("5.List Students")
        print("6.Exit")
        
        choice=input("Enter your Choice")

        if choice=="1":
            add_student()
        elif choice=="2":
            edit_student()
        elif choice=="3":
            del_student()
        elif choice=="4":
            search_student()
        elif choice=="5":
            list_students()
        elif choice=="6":
            print("exiting the system")
            break
        else:
            print("Invalid Choice. Please try again.")

#start the program
if login():
    menu()

