#The username and pass that validates administrator login
username="admin"
password="1234"
#Admin_login takes us to the login page
#here the inputed values are compared to given data for validation
#if correct, then login suucessful
#if not login invalid
def admin_login():
    uname=input("Username: ")
    pwd=input("Password: ")
    if uname==username and pwd==password:
        print("\tLogin Successfull!!!")
        print("\tWelcome Administrator!!!")
        return True
    else:
        print("\tInvalid Credentials!")
        return

#this the dictionary containing all data regarding the customers of bank
#while begining the code, the customer data is empty.
#So the customer dictionary ought be filled first using add_customer().
#Then only can we access customer login.
# customer login can only be done inside admin menu using the confidential data like account noa dn atm pin.  
customers={}
#Add customers()

def add_customer():
    import random
    account_no=random.randint(100000000,999999999)# account number is randomly generated 9 digit number by the computer 
    if account_no in customers:#verifying if account numvber exists or not
        print("\tCustomer already exists!!!")
    else:#if it doesnt
        print("\n \tAccount Number: ",account_no)#values are inputed
        name=input("Enter the Customer Name: ").title()#.title() makes the first letters capital for each word
        if len(name)>30:#length of the name cannot be bigger than 30
                print("Customer Name should not be more than 30 characters!!!")
                return
        type=input("Enter if Account Type is Savings or Current: ").upper()#.upper makes so that anything entered here is in uppercase
        if type!="SAVINGS" and type!="CURRENT":#to make sure only SAVINGS or CURRENT are inputed
            return
        try:#only integers are in balance
            balance=int(input("Enter the account balance: "))
        except ValueError:
            print("Enter only numbers!")
            return
        try:#only integers are in min_bal
            min_bal=int(input("Enter the minimum balance of this account: "))
        except ValueError:
            print("Enter only numbers!")
            return
        if balance<min_bal:#account balance must always be greater than minimum balance
            print("Account Balance must always be greater than minimum balance!")
            return
        try:#mobile nu must always be numerical
            mobile_no=int(input("Enter your mobile no: "))
            if mobile_no<1000000000 or mobile_no>9999999999:#mobile number must always be 10 digit number
                print("A mobile number contains only 10 digits! Try Again!")
                return
        except ValueError:
            print("Enter only numbers!")
            return
        email_id=input("Enter the email id: ")
        pan_number=input("Enter your pan number").upper()
        import random
        ATM_PIN=random.randint(1000,9999)#randomly generated 4 digit number as pin
        customers[account_no]={"Account no: ":account_no,"Customer Name: ":name,"Account type: ":type,"Account Balance: ":balance,"Minimum Balance: ":min_bal,"Customer Mobile No: ":mobile_no,"Customer Email Id: ":email_id,"Customer Pan number: ":pan_number,"ATM PIN: ":ATM_PIN}
        print("\tCustomer Details Entered Sucessfully!!!")

def update_customer():#to update customer details
    try:#account number must be numerical
        account_no=int(input("Enter the Account Number of the Customer whose details you want to update: "))
    except ValueError:
        print("Invalid Account Number. Must be a number.")
        return
    if account_no in customers:#if the account no exists then you can update
        try:
            new_account_no=input(f"Update Customer Account No: [{customers[account_no]['Account no: ']}]") or customers[account_no]['Account no: ']
        except ValueError:
            print("Enter only numbers!")
            return
        try:
            mobile_no=input(f"Update Customer Mobile No: [{customers[account_no]['Customer Mobile No: ']}]") or customers[account_no]['Customer Mobile No: ']
        except ValueError:
            print("Enter only numbers!")
            return
        if mobile_no<1000000000 or mobile_no>9999999999:#mobile number must always be 10 digit number
            print("A mobile number contains only 10 digits! Try Again!")
            return
        email_id=input(f"Update Customer Email Id: [{customers[account_no]['Customer Email Id: ']}]") or customers[account_no]['Customer Email Id: ']
        customers[account_no]={"Account No: ":new_account_no,"Customer Mobile No: ":mobile_no,"Customer Email Id: ":email_id}
        print("\tAccount details updated Successfully!!!")

    else:
        print("No such account exists in the database!")

def delete_customer():#to remove a customer
    try:
        account_no=int(input("Enter the account number of the customer you want to remove: "))
    except ValueError:
        print("Invalid Account Number. Must be a number.")
        return
    if account_no in customers:
        del customers[account_no]
        print("\tCustomer Data Deleted Successfully!")
    else:
        print("\tNo Account that belongs to this ID exists in this Database!")

def view_all_customers():#prints out all the account data stored in the bank database
    if not customers:
        print("\tNo Accounts opened in the Bank!!!")
    else:
        for account_no, info in customers.items():#the loop makes sure that all account details are shown
            print(f"\nAccount Number: ,{info['Account No: ']}")
            print(f"    Customer Name: ,{info['Customer Name: ']}")
            print(f"    Account Type: ,{info['Account Type: ']}")
            print(f"    Account Balance: : {info['Account Balance: ']}")
            print(f"    Minimum Balance: {info['Minimum Balance: ']}")
            print(f"    Customer Mobile No: {info['Customer Mobile No: ']}")
            print(f"    Customer Email Id: {info['Customer Email Id: ']}")
            print(f"    ATM PIN: {info['ATM PIN: ']}")

def find_customer():#to find a specific customer and their details
    try:#you need their account no
        account_no=int(input("Enter the Account Number of the customer you want to find: "))
    except ValueError:#makes sure its a number
        print("Invalid Account Number. Must be a number.")
        return
    if account_no in customers:#check if the number is in the dictionary
        print("Customer Found!")
        print("\n   Account No: ",account_no)
        print("    Customer Name: ",customers[account_no]['Customer Name: '])
        print("    Account Type: ",customers[account_no]['Account Type: '])
        print("    Account Balance: ",customers[account_no]['Account Balance: '])
        print("    Minimum Balance: ",customers[account_no]['Minimum Balance: '])
        print("    Customer Mobile No: ",customers[account_no]['Customer Mobile No: '])
        print("    Customer Email Id: ",customers[account_no]['Customer Email Id: '])
        print("    ATM PIN: ",customers[account_no]['ATM PIN: '])
    else:
        print("Account number not found..!!!")

def customer_login():#here we are entering as a customer using their account no and atm pin. the database should be started and customers must be added before customer can login
    account_no=int(input("Enter the Account No:"))#account no instead of username
    pwd=int(input("Enter your ATM PIN: "))#atm pin instead of password
    if account_no in customers:#if account number in dictionary
        if pwd==customers[account_no]['ATM_PIN']:#and the pin entered is same as the pin in the account number dictionary
            print("\tLogin Successfull!!!")
            print("\tWelcome Customer!!!")
            return customer_menu()
    else:
        print("\tInvalid Credentials!")


def deposit_money():#after customer login only you can deposit money
    try:#only numbers should be entered
        account_no=int(input("Enter your account number: "))
        if account_no not in customers:
            return
        deposit=int(input("Enter the amount to be deposited: ")) 
    except ValueError:
        print("Enter numerical vlue only!")
        return
    if deposit>=50000:#If Amount is greater than 50k then ask the customer to enter his/her PAN Card number
        pan_no=input("Enter pan number")
        if pan_no==customers[account_no]['Pan Number']:
            customers[account_no]["Account Balance: "]+=deposit
            print(f"Your Account Balnce is now {customers[account_no]["Account Balance: "]}")
        else:
            return
    else:
        customers[account_no]["Account Balance: "]+=deposit
        print(f"Your Account Balnce is now {[customers[account_no]["Account Balance: "]]}")
    print("\tMoney successfully deposited!")

def withdraw_money():#after customer login only you can withdraw money
    try:
        account_no=int(input("Enter your account number: "))
        if account_no not in customers:
            return
        withdraw=int(input("Enter the amount to be withdraw: "))
    except ValueError:
        print("Enter numerical vlue only!")
        return
    if withdraw>=50000:#If Amount is greater than 50k then ask the customer to enter his/her PAN Card number
        pan_no=input("Enter pan number")
        if pan_no==customers[account_no]['Pan Number']:
            customers[account_no]["Account Balance: "]+=withdraw
            print(f"Your Account Balnce is now {customers[account_no]["Account Balance: "]}")
        else:
            return
    else:
        customers[account_no]["Account Balance: "]-=withdraw
        if customers[account_no]["Account Balance: "]>=customers[account_no]["Minimum Balance: "]:#the account balance must remain greater than
            print(f"Your Account Balnce is now {[customers[account_no]["Account Balance: "]]}")
            print("\tMoney successfully withdrawn!")
        else:
            customers[account_no]["Account Balance: "]+=withdraw
            print("“Insufficient funds..!!!")


def show_balance():#show balance
    try:
        account_no=int(input("Enter your account number: "))#make sure account in dictionary
        if account_no not in customers:
            return
    except ValueError:
        print("Enter Numerical Values Only!")
    print(f"Your Account Balnce is now {[customers[account_no]["Account Balance: "]]}")


def transfer_money():
    try:
        transfer=int(input("Enter the amount to be transferred"))
        account_no1=int(input("Transferred from: "))
        account_no2=int(input("Transferred to: "))
    except ValueError:
        print("Numerical values only!")
        return
    withdraw_money(account_no1)
    deposit_money(account_no2)
    show_balance(account_no1)
    print("“ Transferred Amount Successfully”")


def admin_menu():
    while True:
        print("\n1. Adding a New Customer")
        print("2. Updating Customer Details")
        print("3. Deleting a Customer")
        print("4. Display the list of all Customers in the Bank")
        print("5. Display Customer Details of a specific Customer")
        print("6. Go to customer login")
        print("7. Exit")

        choice=input("Enter your Choice")
        if choice=="1":
            add_customer()
        elif choice=="2":
            update_customer()
        elif choice=="3":
            delete_customer()
        elif choice=="4": 
            view_all_customers()
        elif choice=="5": 
            find_customer()
        elif choice=="6": 
            customer_login()
        elif choice=="7": 
            print("\tExiting the system...")
            break
        else:
            print("\tInvalid Choice. Please Try again.")

def customer_menu():
    while True:
        print("\n1. Depositing Money into Customer Account")
        print("2. Withdraw Money from Customer Account")
        print("3. Show Balance of a Customer")
        print("4. Transferring Money from One Account to Another account")
        print("5. exit")

        choice=input("Enter your Choice")
        if choice=="1":
            deposit_money()
        elif choice=="2":
            withdraw_money()
        elif choice=="3":
            show_balance()
        elif choice=="4": 
            transfer_money()
        elif choice=="5": 
            print("\tExiting the system...")
            break
        else:
            print("\tInvalid Choice. Please Try again.")

def main():
    if admin_login():
        admin_menu()
    else:
        print("Try Again!")
        return
main()
