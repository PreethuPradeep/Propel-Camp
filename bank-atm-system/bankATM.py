import random

username = "admin"
password = "1234"

customers = {}

def admin_login():
    uname = input("Username: ")
    pwd = input("Password: ")
    if uname == username and pwd == password:
        print("\tLogin Successful!!!")
        print("\tWelcome Administrator!!!")
        return True
    else:
        print("\tInvalid Credentials!")
        return False

def add_customer():
    account_no = random.randint(100000000, 999999999)
    if account_no in customers:
        print("\tCustomer already exists!!!")
        return
    print("\n\tAccount Number: ", account_no)
    name = input("Enter the Customer Name: ").title()
    if len(name) > 30:
        print("Customer Name should not be more than 30 characters!!!")
        return
    acc_type = input("Enter if Account Type is Savings or Current: ").upper()
    if acc_type not in ("SAVINGS", "CURRENT"):
        print("Invalid Account Type! Must be SAVINGS or CURRENT.")
        return
    try:
        balance = int(input("Enter the account balance: "))
    except ValueError:
        print("Enter only numbers!")
        return
    try:
        min_bal = int(input("Enter the minimum balance of this account: "))
    except ValueError:
        print("Enter only numbers!")
        return
    if balance < min_bal:
        print("Account Balance must always be greater than minimum balance!")
        return
    try:
        mobile_no = int(input("Enter your mobile no: "))
        if mobile_no < 1000000000 or mobile_no > 9999999999:
            print("A mobile number contains only 10 digits! Try Again!")
            return
    except ValueError:
        print("Enter only numbers!")
        return
    email_id = input("Enter the email id: ")
    pan_number = input("Enter your PAN number: ").upper()
    ATM_PIN = random.randint(1000, 9999)
    customers[account_no] = {
        "Account No: ": account_no,
        "Customer Name: ": name,
        "Account Type: ": acc_type,
        "Account Balance: ": balance,
        "Minimum Balance: ": min_bal,
        "Customer Mobile No: ": mobile_no,
        "Customer Email Id: ": email_id,
        "Customer Pan Number: ": pan_number,
        "ATM PIN: ": ATM_PIN
    }
    print(f"\tCustomer Details Entered Successfully! Your ATM PIN is {ATM_PIN}")

def update_customer():
    try:
        account_no = int(input("Enter the Account Number of the Customer to update: "))
    except ValueError:
        print("Invalid Account Number. Must be a number.")
        return
    if account_no in customers:
        customer = customers[account_no]
        new_mobile = input(f"Update Customer Mobile No [{customer['Customer Mobile No: ']}]: ") or str(customer['Customer Mobile No: '])
        try:
            new_mobile_int = int(new_mobile)
            if new_mobile_int < 1000000000 or new_mobile_int > 9999999999:
                print("Mobile number must be 10 digits.")
                return
        except ValueError:
            print("Enter only numbers for mobile no.")
            return
        new_email = input(f"Update Customer Email Id [{customer['Customer Email Id: ']}]: ") or customer['Customer Email Id: ']
        # Update fields
        customer['Customer Mobile No: '] = new_mobile_int
        customer['Customer Email Id: '] = new_email
        print("\tAccount details updated Successfully!!!")
    else:
        print("No such account exists in the database!")

def deposit_money():
    try:
        account_no = int(input("Enter your account number: "))
        if account_no not in customers:
            print("Account not found.")
            return
        deposit = int(input("Enter the amount to be deposited: "))
    except ValueError:
        print("Enter numerical value only!")
        return
    if deposit >= 50000:
        pan_no = input("Enter PAN number: ").upper()
        if pan_no != customers[account_no]['Customer Pan Number: ']:
            print("PAN number mismatch! Deposit cancelled.")
            return
    customers[account_no]["Account Balance: "] += deposit
    print(f"Your Account Balance is now {customers[account_no]['Account Balance: ']}")
    print("\tMoney successfully deposited!")

def withdraw_money():
    try:
        account_no = int(input("Enter your account number: "))
        if account_no not in customers:
            print("Account not found.")
            return
        withdraw = int(input("Enter the amount to be withdrawn: "))
    except ValueError:
        print("Enter numerical value only!")
        return
    if withdraw >= 50000:
        pan_no = input("Enter PAN number: ").upper()
        if pan_no != customers[account_no]['Customer Pan Number: ']:
            print("PAN number mismatch! Withdrawal cancelled.")
            return
    if customers[account_no]["Account Balance: "] - withdraw >= customers[account_no]["Minimum Balance: "]:
        customers[account_no]["Account Balance: "] -= withdraw
        print(f"Your Account Balance is now {customers[account_no]['Account Balance: ']}")
        print("\tMoney successfully withdrawn!")
    else:
        print("Insufficient funds..!!!")

def customer_login():
    try:
        account_no = int(input("Enter the Account No: "))
        pwd = int(input("Enter your ATM PIN: "))
    except ValueError:
        print("Account number and PIN must be numeric.")
        return
    if account_no in customers:
        if pwd == customers[account_no]['ATM PIN: ']:
            print("\tLogin Successful!!!")
            print("\tWelcome Customer!!!")
            customer_menu(account_no)
        else:
            print("\tInvalid PIN!")
    else:
        print("\tInvalid Account Number!")

def show_balance(account_no):
    print(f"Your Account Balance is now {customers[account_no]['Account Balance: ']}")

def transfer_money(account_no_from):
    try:
        amount = int(input("Enter the amount to be transferred: "))
        account_no_to = int(input("Transferred to (Account No): "))
    except ValueError:
        print("Numerical values only!")
        return
    if account_no_to not in customers:
        print("Receiver account not found!")
        return
    if customers[account_no_from]["Account Balance: "] - amount < customers[account_no_from]["Minimum Balance: "]:
        print("Insufficient funds for transfer.")
        return
    customers[account_no_from]["Account Balance: "] -= amount
    customers[account_no_to]["Account Balance: "] += amount
    print(f"Transferred {amount} from account {account_no_from} to {account_no_to} successfully.")
    show_balance(account_no_from)

def customer_menu(account_no):
    while True:
        print("\n1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Show Balance")
        print("4. Transfer Money")
        print("5. Logout")
        choice = input("Enter your Choice: ")
        if choice == "1":
            deposit_money()
        elif choice == "2":
            withdraw_money()
        elif choice == "3":
            show_balance(account_no)
        elif choice == "4":
            transfer_money(account_no)
        elif choice == "5":
            print("\tLogging out...")
            break
        else:
            print("\tInvalid Choice. Please Try again.")

def admin_menu():
    while True:
        print("\n1. Add Customer")
        print("2. Update Customer Details")
        print("3. Delete Customer")
        print("4. View All Customers")
        print("5. Find Customer by Account Number")
        print("6. Customer Login")
        print("7. Exit")
        choice = input("Enter your Choice: ")
        if choice == "1":
            add_customer()
        elif choice == "2":
            update_customer()
        elif choice == "3":
            delete_customer()
        elif choice == "4":
            view_all_customers()
        elif choice == "5":
            find_customer()
        elif choice == "6":
            customer_login()
        elif choice == "7":
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

