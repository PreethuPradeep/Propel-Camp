# User credentials
username1 = "admin"
password1 = "1234"
username2 = "recept"
password2 = "1234"
username3 = "pharm"
password3 = "1234"
username4 = "labtech"
password4 = "1234"

# Data stores
patients = {}
staffs = {}
medicines = {}
tests = {}

# Login function
def login():
    uname = input("Username: ")
    pwd = input("Password: ")
    if uname == username1 and pwd == password1:
        print("Login Successful!")
        return admin_menu()
    elif uname == username2 and pwd == password2:
        print("Login Successful!")
        return recept_menu()
    elif uname == username3 and pwd == password3:
        print("Login Successful!")
        return pharm_menu()
    elif uname == username4 and pwd == password4:
        print("Login Successful!")
        return lab_menu()
    else:
        print("Invalid Credentials!")
        return False

# --- Patient Functions ---

def add_patient():
    patient_id = input("Enter patient Id: ")
    if patient_id in patients:
        print("Patient already exists!")
        return
    name = input("Enter the patient Name: ").title()
    try:
        age = int(input("Enter the patient Age: "))
    except:
        print("Enter numbers only for Age!")
        return
    address = input("Enter the patient Address: ").title()
    disease = input("Enter the patient disease: ").title()
    blood_group = input("Enter the patient Blood Group: ").upper()
    try:
        weight = float(input("Enter the patient weight: "))
    except:
        print("Error. Please enter only numbers for weight!")
        return
    try:
        height = float(input("Enter the patient height: "))
    except:
        print("Error. Please enter only numbers for height!")
        return
    try:
        phoneNumber = int(input("Enter the patient Phone number: "))
    except:
        print("Error. Please enter only numbers for phone number!")
        return

    patients[patient_id] = {
        "Name: ": name,
        "Age: ": age,
        "Address: ": address,
        "Disease: ": disease,
        "Blood Group: ": blood_group,
        "Weight: ": weight,
        "Height: ": height,
        "Phone Number: ": phoneNumber
    }
    print("Patient details successfully added!")

def View_patients():
    if not patients:
        print("No patients currently admitted.")
    else:
        for patient_id, info in patients.items():
            print("\n")
            print(f"Patient ID: {patient_id}")
            for key, val in info.items():
                print(f"{key} {val}")

def Search_patient():
    patient_id = input("Enter the Id of the patient you want to find: ")
    if patient_id in patients:
        print("\nPatient Found!")
        print(f"\tPatient Id: {patient_id}")
        for key, val in patients[patient_id].items():
            print(f"\t{key} {val}")
        print()
    else:
        print("Patient not Found!")

def Update_records():
    patient_id = input("Enter the Id of the patient you want to update: ")
    if patient_id in patients:
        print("Enter new Details... or leave empty for no changes")
        current = patients[patient_id]
        Name = input(f"Update Name [{current['Name: ']}]: ") or current['Name: ']
        try:
            Age_input = input(f"Update Age [{current['Age: ']}]: ")
            Age = int(Age_input) if Age_input else current['Age: ']
        except:
            print("Only numbers are accepted for Age!")
            return
        Address = input(f"Update Address [{current['Address: ']}]: ") or current['Address: ']
        Disease = input(f"Update Disease [{current['Disease: ']}]: ") or current['Disease: ']
        Blood_Group = input(f"Update Blood Group [{current['Blood Group: ']}]: ") or current['Blood Group: ']
        try:
            Weight_input = input(f"Update Weight [{current['Weight: ']}]: ")
            Weight = float(Weight_input) if Weight_input else current['Weight: ']
        except:
            print("Only numbers are accepted for Weight!")
            return
        try:
            Height_input = input(f"Update Height [{current['Height: ']}]: ")
            Height = float(Height_input) if Height_input else current['Height: ']
        except:
            print("Only numbers are accepted for Height!")
            return
        try:
            Phone_input = input(f"Update Phone Number [{current['Phone Number: ']}]: ")
            Phone_Number = int(Phone_input) if Phone_input else current['Phone Number: ']
        except:
            print("Only numbers are accepted for Phone Number!")
            return

        patients[patient_id] = {
            "Name: ": Name,
            "Age: ": Age,
            "Address: ": Address,
            "Disease: ": Disease,
            "Blood Group: ": Blood_Group,
            "Weight: ": Weight,
            "Height: ": Height,
            "Phone Number: ": Phone_Number
        }
        print("Patient details updated successfully!")
    else:
        print("Patient not found.")

def Delete_record():
    patient_id = input("Enter the id of the patient you want to remove: ")
    if patient_id in patients:
        del patients[patient_id]
        print("Patient details successfully deleted!")
    else:
        print("No such patient exists in the system!")

# --- Staff Functions ---

def add_staff():
    staff_id = input("Enter staff Id: ")
    if staff_id in staffs:
        print("Staff Member already exists!")
        return
    name = input("Enter the Staff Member Name: ").title()
    designation = input("Enter the Staff Member designation: ").title()
    location = input("Enter the Staff Member location: ").title()
    dateOfJoining = input("Enter the Staff Member date of joining: ")
    try:
        salary = float(input("Enter the Staff Member salary: "))
    except:
        print("Error. Please enter only numbers for salary!")
        return
    try:
        age = int(input("Enter the Staff Member age: "))
    except:
        print("Error. Please enter only numbers for age!")
        return
    try:
        phoneNumber = int(input("Enter the Staff Member Phone number: "))
    except:
        print("Error. Please enter only numbers for phone number!")
        return

    staffs[staff_id] = {
        "Name: ": name,
        "Age: ": age,
        "Designation: ": designation,
        "Location: ": location,
        "Date Of Joining: ": dateOfJoining,
        "Salary: ": salary,
        "Phone Number: ": phoneNumber
    }
    print("Staff Member details successfully added!")

def View_staff():
    if not staffs:
        print("No Staff members currently admitted.")
    else:
        for staff_id, info in staffs.items():
            print("\n")
            print(f"Staff ID: {staff_id}")
            for key, val in info.items():
                print(f"{key} {val}")

def Search_staff():
    staff_id = input("Enter the Id of the staff you want to find: ")
    if staff_id in staffs:
        print("\nStaff Found!")
        print(f"\tStaff Id: {staff_id}")
        for key, val in staffs[staff_id].items():
            print(f"\t{key} {val}")
        print()
    else:
        print("Staff not Found!")

def Update_staff():
    staff_id = input("Enter the Id of the staff you want to update: ")
    if staff_id in staffs:
        print("Enter new Details... or leave empty for no changes")
        current = staffs[staff_id]

        Name = input(f"Update Name [{current['Name: ']}]: ") or current['Name: ']
        try:
            Age_input = input(f"Update Age [{current['Age: ']}]: ")
            Age = int(Age_input) if Age_input else current['Age: ']
        except:
            print("Only numbers are accepted for Age!")
            return
        Designation = input(f"Update Designation [{current['Designation: ']}]: ") or current['Designation: ']
        dateOfJoining = input(f"Update Date Of Joining [{current['Date Of Joining: ']}]: ") or current['Date Of Joining: ']
        Location = input(f"Update Location [{current['Location: ']}]: ") or current['Location: ']
        try:
            Salary_input = input(f"Update Salary [{current['Salary: ']}]: ")
            Salary = float(Salary_input) if Salary_input else current['Salary: ']
        except:
            print("Only numbers are accepted for Salary!")
            return
        try:
            Phone_input = input(f"Update Phone Number [{current['Phone Number: ']}]: ")
            Phone_Number = int(Phone_input) if Phone_input else current['Phone Number: ']
        except:
            print("Only numbers are accepted for Phone Number!")
            return

        staffs[staff_id] = {
            "Name: ": Name,
            "Age: ": Age,
            "Designation: ": Designation,
            "Date Of Joining: ": dateOfJoining,
            "Location: ": Location,
            "Salary: ": Salary,
            "Phone Number: ": Phone_Number
        }
        print("Staff details updated successfully!")
    else:
        print("Staff ID not recognized. Try again.")

def Delete_staff():
    staff_id = input("Enter the staff id you want to delete: ")
    if staff_id in staffs:
        del staffs[staff_id]
        print("Staff id deleted successfully!")
    else:
        print("No such staff exists in the system!")

# --- Medicine Functions ---

def add_Medicine():
    medicine_id = input("Enter the medicine id: ")
    if medicine_id in medicines:
        print("Medicine already exists!")
        return
    medicine_name = input("Enter the Medicine Name: ").title()
    generic_name = input("Enter the generic name of the medicine: ").title()
    company_name = input("Enter the Company name: ").title()
    try:
        price = float(input("Enter the price of the medicine: "))
    except:
        print("Enter numbers only for price!")
        return

    medicines[medicine_id] = {
        "Name: ": medicine_name,
        "Generic Name: ": generic_name,
        "Company Name: ": company_name,
        "Price: ": price
    }
    print("Medicine details successfully added!")

def View_Medicine():
    if not medicines:
        print("No medicines currently entered!")
    else:
        for medicine_id, info in medicines.items():
            print(f"\nMedicine ID: {medicine_id}")
            for key, val in info.items():
                print(f"{key} {val}")

def Update_Medicine():
    medicine_id = input("Enter the medicine id you want to update: ")
    if medicine_id in medicines:
        print("Enter new Details... or leave empty for no changes")
        current = medicines[medicine_id]
        Name = input(f"Update Medicine Name [{current['Name: ']}]: ") or current['Name: ']
        Generic_Name = input(f"Update Generic Name [{current['Generic Name: ']}]: ") or current['Generic Name: ']
        Company_Name = input(f"Update Company Name [{current['Company Name: ']}]: ") or current['Company Name: ']
        try:
            Price_input = input(f"Update Price [{current['Price: ']}]: ")
            Price = float(Price_input) if Price_input else current['Price: ']
        except:
            print("Enter numbers only for price!")
            return

        medicines[medicine_id] = {
            "Name: ": Name,
            "Generic Name: ": Generic_Name,
            "Company Name: ": Company_Name,
            "Price: ": Price
        }
        print("Medicine details updated successfully!")
    else:
        print("No such medicine exists in the system!")

def Delete_Medicine():
    medicine_id = input("Enter the medicine id you want to delete: ")
    if medicine_id in medicines:
        del medicines[medicine_id]
        print("Medicine id deleted successfully!")
    else:
        print("No such medicine exists in the system!")

# --- Lab Test Functions ---

def add_test():
    test_id = input("Enter the test id: ")
    if test_id in tests:
        print("Test already exists!")
        return
    test_name = input("Enter the test name: ").title()
    try:
        test_cost = float(input("Enter the test cost: "))
    except:
        print("Error. Enter numbers only!")
        return
    tests[test_id] = {
        "Test Name: ": test_name,
        "Test Cost: ": test_cost
    }
    print("Test details successfully added!")

def View_tests():
    if not tests:
        print("No lab tests currently entered!")
    else:
        for test_id, info in tests.items():
            print(f"\nTest ID: {test_id}")
            for key, val in info.items():
                print(f"{key} {val}")

def Update_Test():
    test_id = input("Enter the test id you want to update: ")
    if test_id in tests:
        print("Enter new Details... or leave empty for no changes")
        current = tests[test_id]
        test_name = input(f"Update Test Name [{current['Test Name: ']}]: ") or current['Test Name: ']
        try:
            cost_input = input(f"Update Test Cost [{current['Test Cost: ']}]: ")
            test_cost = float(cost_input) if cost_input else current['Test Cost: ']
        except:
            print("Enter numbers only for cost!")
            return

        tests[test_id] = {
            "Test Name: ": test_name,
            "Test Cost: ": test_cost
        }
        print("Test details updated successfully!")
    else:
        print("No such test exists in the system!")

def Delete_Test():
    test_id = input("Enter the test id you want to delete: ")
    if test_id in tests:
        del tests[test_id]
        print("Test id deleted successfully!")
    else:
        print("No such test exists in the system!")

# --- Menus ---

def admin_menu():
    while True:
        print("\nWelcome Admin")
        print("1. Patient Menu")
        print("2. Staff Menu")
        print("3. Medicine Menu")
        print("4. Lab Menu")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            patient_menu()
        elif choice == "2":
            staff_menu()
        elif choice == "3":
            pharm_menu()
        elif choice == "4":
            lab_menu()
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid Choice. Try again.")

def patient_menu():
    while True:
        print("\nPatient Menu")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Back to Admin Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            View_patients()
        elif choice == "3":
            Search_patient()
        elif choice == "4":
            Update_records()
        elif choice == "5":
            Delete_record()
        elif choice == "6":
            break
        else:
            print("Invalid Choice. Try again.")

def staff_menu():
    while True:
        print("\nStaff Menu")
        print("1. Add Staff")
        print("2. View Staff")
        print("3. Search Staff")
        print("4. Update Staff")
        print("5. Delete Staff")
        print("6. Back to Admin Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_staff()
        elif choice == "2":
            View_staff()
        elif choice == "3":
            Search_staff()
        elif choice == "4":
            Update_staff()
        elif choice == "5":
            Delete_staff()
        elif choice == "6":
            break
        else:
            print("Invalid Choice. Try again.")

def pharm_menu():
    while True:
        print("\nPharmacy Menu")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Update Medicine")
        print("4. Delete Medicine")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_Medicine()
        elif choice == "2":
            View_Medicine()
        elif choice == "3":
            Update_Medicine()
        elif choice == "4":
            Delete_Medicine()
        elif choice == "5":
            break
        else:
            print("Invalid Choice. Try again.")

def lab_menu():
    while True:
        print("\nLab Menu")
        print("1. Add Test")
        print("2. View Tests")
        print("3. Delete Test")
        print("4. Update Test")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_test()
        elif choice == "2":
            View_tests()
        elif choice == "3":
            Delete_Test()
        elif choice == "4":
            Update_Test()
        elif choice == "5":
            break
        else:
            print("Invalid Choice. Try again.")

def recept_menu():
    while True:
        print("\nReceptionist Menu")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            View_patients()
        elif choice == "3":
            Search_patient()
        elif choice == "4":
            Update_records()
        elif choice == "5":
            Delete_record()
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("Invalid Choice. Try again.")

# Main program starts here
while True:
    if not login():
        print("Login Failed. Try again or press Ctrl+C to exit.")
