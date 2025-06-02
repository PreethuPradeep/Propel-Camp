username1="admin"
password1="1234"
username2="recept"
password2="1234"
username3="pharm"
password3="1234"
username4="labtech"
password4="1234"

def login():
    uname=input("Username: ")
    pwd=input("Password: ")
    if uname==username1 and pwd==password1:
        print("Login Successful!")
        return admin_menu()
    if uname==username2 and pwd==password2:
        print("Login Successful!")
        return recept_menu()
    if uname==username3 and pwd==password3:
        print("Login Successful!")
        return pharm_menu()
    if uname==username4 and pwd==password4:
        print("Login Successful!")
        return lab_menu()
    else:
        print("Invalid Credentials!")
        return False

patients={}
staffs={}
medicines={}
tests={}

def add_patient():
    patient_id=input("Enter patient Id: ")
    if patient_id in patients:
        print("Patient already exists!")
        return
    name=input("Enter the patient Name: ").title()
    try:
        age=int(input("Enter the patient Age: "))
    except:
        print("Enter numbers only")
        return
    address=input("Enter the patient Address: ").title()
    disease=input("Enter the patient disease: ").title()
    blood_group=input("Enter the patient Blood Group: ").upper()
    try:
        weight=float(input("Enter the patient weight: "))
    except:
        print("Error. Please enter only numbers!")
        return
    try:
        height=float(input("Enter the patient height: "))
    except:
        print("Error. Please enter only numbers!")
        return
    try:
        phoneNumber=int(input("Enter the patient Phone number: "))
    except:
        print("Error. Please enter only numbers!")
        return
    try:
        patients[patient_id]={"Name: ":name,"Age: ":age,"Address: ":address,"Disease: ":disease,"Blood Group: ":blood_group,"weight: ":weight,"height: ":height,"Phone Number: ":phoneNumber}
    except:
        print("Error. Please try again.")
        return
    print("Patient Detailes successfully added!")


def View_patients():
    if not patients:
        print("No patients currently admitted.")
    else:
        for patient_id, info in patients.items():
            print(" ")
            print(f"{patient_id}. ,\nPatient's Name: {info['Name: ']},\nAge: {info['Age: ']},\nAddress: {info['Address: ']},\nDisease: {info['Disease: ']},\nBlood Group: {info['Blood Group: ']},\nweight: {info['weight: ']},\nheight: {info['height: ']},\nPhone Number: {info['Phone Number: ']}\n")

def Search_patient():
    patient_id=input("Enter the Id of the patient you want to find: ")
    if patient_id in patients:
        print(" ")
        print("Patient Found!")
        print("\tPatient Id: ",patient_id)
        print("\tPatient's Name: ",patients[patient_id]['Name: '])
        print("\tAge: ",patients[patient_id]['Age: '])
        print("\tAddress: ",patients[patient_id]['Address: '])
        print("\tDisease: ",patients[patient_id]['Disease: '])
        print("\tBlood Group: ",patients[patient_id]['Blood Group: '])
        print("\tWeight: ",patients[patient_id]['weight: '])
        print("\tHeight: ",patients[patient_id]['height: '])
        print("\tPhone Number: ",patients[patient_id]['Phone Number: '])
        print(" ")
    else:
        print("Patient not Found!")

def Update_records():
    patient_id=input("Enter the Id of the patient you want to update: ")
    if patient_id in patients:
        print("Enter new Details... or leave empty for no changes")
        Name=input(f"Update Name: [{patients[patient_id]['Name: ']}]") or patients[patient_id]['Name: ']
        try:
            Age=int(input(f"Update Age: [{patients[patient_id]['Age: ']}]")) or patients[patient_id]['Age: ']
        except:
            print("Only numbers are accepted!")
            return
        Address=input(f"Update Address: [{patients[patient_id]['Address: ']}]") or patients[patient_id]['Age: ']
        Disease=input(f"Update Disease: [{patients[patient_id]['Disease: ']}]") or patients[patient_id]['Disease: ']
        Blood_Group=input(f"Update Blood Group: [{patients[patient_id]['Blood Group: ']}]") or patients[patient_id]['Blood Group: ']
        try:
            Weight=float(input(f"Update weight: [{patients[patient_id]['weight: ']}]") or patients[patient_id]['weight: '])
        except:
            print("Only numbers are accepted!")
            return
        try:
            Height=input(f"Update height: [{patients[patient_id]['height: ']}]") or patients[patient_id]['height: ']
        except:
            print("Only numbers are accepted!")
            return
        try:
            Phone_Number=input(f"Update Phone Number: [{patients[patient_id]['Phone Number: ']}]") or patients[patient_id]['Phone Number: ']
        except:
            print("Only numbers are accepted!")
            return
        try:
            patients[patient_id]={"Name: ":Name,"Age: ":Age,"Address: ":Address,"Disease: ":Disease,"Blood Group: ":Blood_Group,"Weight: ":Weight,"Height: ":Height,"Phone Number: ":Phone_Number}
        except:
            print("Try again!")
            return
        print("Patient details Updated successfully!")

def Delete_record():
    patient_id=input("Enter the id of the patient who you wnat to remove: ")
    if patient_id in patients:
        del patients[patient_id]
        print("Patient details succsesfully deleted!")
    else:
        print("No such patient exists in the system!")


def add_staff():
    staff_id=input("Enter staff Id: ")
    if staff_id in staffs:
        print("Staff Member already exists!")
        return
    name=input("Enter the Staff Member Name: ").title()
    designation=input("Enter the Staff Member designation").title()
    location=input("Enter the Staff Member location: ").title()
    dateOfJoining=input("Enter the Staff Member date of joining: ")
    try:
        salary=float(input("Enter the Staff Member salary: "))
    except:
        print("Error. Please enter only numbers!")
        return
    try:
        age=int(input("Enter the Staff Member age: "))
    except:
        print("Error. Please enter only numbers!")
        return
    try:
        phoneNumber=int(input("Enter the Staff Member Phone number: "))
    except:
        print("Error. Please enter only numbers!")
        return
    try:
        staffs[staff_id]={"Name: ":name,"Age: ":age,"Designation: ":designation,"Location: ":location,"Date Of Joining: ":dateOfJoining,"Salary: ":salary,"Phone Number: ":phoneNumber}
    except:
        print("Error. Please try again.")
        return
    print("Staff Member Detailes successfully added!")

def View_staff():
    if not staffs:
        print("No Staff members currently admitted.")
    else:
        for staff_id, info in staffs.items():
            print(" ")
            print(f"{staff_id}. ,\nStaff's Name: {info['Name: ']},\nAge: {info['Age: ']},\nDesignation: {info['Designation: ']},\nDate Of Joining: {info['dateOfJoining: ']},\nLocation: {info['location: ']},\nSalary: {info['salary: ']},\nPhone Number: {info['Phone Number: ']}\n")


def Search_staff():
    staff_id=input("Enter the Id of the staff you want to find: ")
    if staff_id in staffs:
        print(" ")
        print("Staff Found!")
        print("\tStaff Id: ",staff_id)
        print("\tStaff's Name: ",staffs[staff_id]['Name: '])
        print("\tStaff's Age: ",staffs[staff_id]['Age: '])
        print("\tDesignation: ",staffs[staff_id]['Designation: '])
        print("\tDate Of Joining: ",staffs[staff_id]['Date Of Joining: '])
        print("\tLocation: ",staffs[staff_id]['Location: '])
        print("\tSalary: ",staffs[staff_id]['Salary: '])
        print("\tPhone Number: ",staffs[staff_id]['Phone Number: '])
        print(" ")
    else:
        print("Patient not Found!")


def Update_staff():
    staff_id=input("Enter the Id of the staff you want to update: ")
    if staff_id in staffs:
        print("Enter new Details... or leave empty for no changes")
        Name=input(f"Update Name: [{staffs[staff_id]['Name: ']}]") or staffs[staff_id]['Name: ']
        try:
            Age=int(input(f"Update Age: [{staffs[staff_id]['Age: ']}]")) or staffs[staff_id]['Age: ']
        except:
            print("Only numbers are accepted!")
            return
        Designation=input(f"Update Designation: [{staffs[staff_id]['Designation: ']}]") or staffs[staff_id]['Age: ']
        dateOfJoining=input(f"Update Date Of Joining: [{staffs[staff_id]['Date Of Joining: ']}]") or staffs[staff_id]['Date Of Joining: ']
        Location=input(f"Update Location: [{staffs[staff_id]['Location: ']}]") or staffs[staff_id]['Location: ']
        try:
            Salary=input(f"Update Salary: [{staffs[staff_id]['Salary: ']}]") or staffs[staff_id]['Salary: ']
        except:
            print("Only numbers are accepted!")
            return
        try:
            Phone_Number=input(f"Update Phone Number: [{staffs[staff_id]['Phone Number: ']}]") or staffs[staff_id]['Phone Number: ']
        except:
            print("Only numbers are accepted!")
            return
        try:
            staffs[staff_id]={"Name: ":Name,"Age: ":Age,"Designation: ":Designation,"Date Of Joining: ":dateOfJoining,"Location: ":Location,"Salary: ":Salary,"Phone Number: ":Phone_Number}
        except:
            print("Try again!")
            return
        print("Staff details Updated successfully!")
    else:
        print("Staff id not recognized. Try")


def Delete_staff():
    staff_id=input("Enter the staff id you want to delete: ")
    if staff_id in staffs:
        del staffs[staff_id]
        print("Staff id deleted Successfully")
    else:
        print("No such staff exists in system!")


def add_Medicine():
    medicine_id=input("Enter the medicine id: ")
    if medicine_id in medicines:
        print("Medicine already exists!")
        return
    medicine_name=input("Enter the Medicine Name: ").title()
    generic_name=input("Enter the generic name of the medicine").title
    company_name=input("Enter the Company name: ").title()
    try:
        price=int(input("Enter the price of the medicine: "))
    except:
        print("Enter numbers only!")
        return

def View_Medicine():
    if not medicines:
        print("No medicines currently entered!")
    else:
        for medicine_id, info in medicines.items():
            print(" ")
            print(f"{medicine_id}. ,\nmedicine's Name: {info['medicine_name: ']},\nGeneric Name: {info['generic_name: ']},\nCompany Name: {info['company_name: ']},\nPrice: {info['price: ']}\n")

def Search_Medicine():
    medicine_id=input("Enter the Id of the medicine you want to find: ")
    if medicine_id in medicines:
        print(" ")
        print("medicine Found!")
        print("\tmedicine Id: ",medicine_id)
        print("\tmedicine's Name: ",medicines[medicine_id]['Name: '])
        print("\tGeneric Name: ",medicines[medicine_id]['Generic Name: '])
        print("\tCompany's Name: ",medicines[medicine_id]['Company Name: '])
        print("\tPrice: ",medicines[medicine_id]['Price: '])
        print(" ")
    else:
        print("medicine not Found!")

def Update_Medicine():
    medicine_id=input("Enter the Id of the medicine you want to update: ")
    if medicine_id in medicines:
        print("Enter new Details... or leave empty for no changes")
        Name=input(f"Update Name: [{medicines[medicine_id]['Name: ']}]") or medicines[medicine_id]['Name: ']
        generic_name=input(f"Update generic name: [{medicines[medicine_id]['generic_name: ']}]") or medicines[medicine_id]['generic_name: ']
        
        Company_Name=input(f"Update Company Name: [{medicines[medicine_id]['Company Name: ']}]") or medicines[medicine_id]['Company Name: ']
        try:
            price=float(input(f"Update price: [{medicines[medicine_id]['price: ']}]") or medicines[medicine_id]['price: '])
        except:
            print("Only numbers are accepted!")
            return
        
        try:
            medicines[medicine_id]={"Name: ":Name,"Generic name: ":generic_name,"Company Name: ":Company_Name,"Price: ":price}
        except:
            print("Try again!")
            return
        print("Medicine details Updated successfully!")


def add_Test():
    test_id=input("Enter new test id: ").upper()
    test_name=input("Enter the test name: ").title()
    try:
        minimum_range=float(input("Enter the minimum range of test results: "))
    except:
        print("Enter numbers only!")
        return
    try:
        maximum_range=float(input("Enter the maximum range of test results: "))
    except:
        print("Enter numbers only!")
        return
    try:
        price=float(input("Enter the cost of the test: "))
    except:
        print("Enter numbers only!")
        return
    

def View_Test():
    if not tests:
        print("No Tests currently entered!")
    else:
        for test_id, info in tests.items():
            print(" ")
            print(f"{test_id}. ,\nTest's Name: {info['test_name: ']},\nMinimum_Range: {info['minimum_range: ']},\nMaximum_Range: {info['maximum_range: ']},\nPrice: {info['price: ']}\n")


def Search_Test():
    test_id=input("Enter the Id of the Test you want to find: ")
    if test_id in tests:
        print(" ")
        print("Test Found!")
        print("\ttest Id: ",test_id)
        print("\ttest's Name: ",tests[test_id]['Name: '])
        print("\tMinimum Range: ",tests[test_id]['Minimum Range: '])
        print("\tMaximum Range: ",tests[test_id]['Maximum Range: '])
        print("\tPrice: ",tests[test_id]['price: '])
        print(" ")
    else:
        print("Test not Found!")
        

        




def Delete_Test():
    test_id=input("Enter the id of the test who you wnat to remove: ")
    if test_id in tests:
        del tests[test_id]
        print("test details succsesfully deleted!")
    else:
        print("No such test exists in the system!")

def Delete_Medicine():
    medicine_id=input("Enter the id of the medicine who you wnat to remove: ")
    if medicine_id in medicines:
        del medicines[medicine_id]
        print("medicine details succsesfully deleted!")
    else:
        print("No such medicine exists in the system!")



def recept_menu():
    while True:
        print("Menu: ")
        print("\tPatient Mangement")
        print("\t1.Add a new Patient")
        print("\t2.View all patients")
        print("\t3.Search for a patient")
        print("\t4.Update an existing patients information")
        print("\t5.Delete a patient record")
        print("\t6.Exit System")

        choice=input("\nEnter your choice")
        if choice=="1":
            add_patient()
        elif choice=="2":
            View_patients()
        elif choice=="3":
            Search_patient()
        elif choice=="4":
            Update_records()
        elif choice=="5":
            Delete_record()
        elif choice=="6":
            print("Exiting the system...")
            login()

        else:
            print("Invalid Choice.Please try again.")

def admin_menu():
    while True:
        print("Admin Menu: ")
        print("\tStaff Mangement")
        print("\t1.Add a new Staff Member")
        print("\t2.View all Staff details")
        print("\t3.Search for a Staff Member")
        print("\t4.Update an existing Staff Member's information")
        print("\t5.Delete a Staff Member's record")
        print("\t6.Exit System")

        choice=input("\nEnter your choice")
        if choice=="1":
            add_staff()
        elif choice=="2":
            View_staff()
        elif choice=="3":
            Search_staff()
        elif choice=="4":
            Update_staff()
        elif choice=="5":
            Delete_staff()
        elif choice=="6":
            print("Exiting the system...")
            login()
        else:
            print("Invalid Choice.Please try again.")

def pharm_menu():
    while True:
        print("Pharmacist Menu: ")
        print("\tMedicine Mangement")
        print("\t1.Add a New Medicine")
        print("\t2.View all Medicine details")
        print("\t3.Search for a Medicine")
        print("\t4.Update an existing Medicine's information")
        print("\t5.Delete a Medicine")
        print("\t6.Exit System")

        choice=input("\nEnter your choice")
        if choice=="1":
            add_Medicine()
        elif choice=="2":
            View_Medicine()
        elif choice=="3":
            Search_Medicine()
        elif choice=="4":
            Update_Medicine()
        elif choice=="5":
            Delete_Medicine()
        elif choice=="6":
            print("Exiting the system...")
            login()
        else:
            print("Invalid Choice.Please try again.")

def lab_menu():
    while True:
        print("Lab Technitian Menu: ")
        print("\tTest Mangement")
        print("\t1.Add a new Test details")
        print("\t2.View all Test details")
        print("\t3.Search for a Test")
        print("\t4.Update an existing Test's information")
        print("\t5.Delete a Test")
        print("\t6.Exit System")

        choice=input("\nEnter your choice")
        if choice=="1":
            add_Test()
        elif choice=="2":
            View_Test()
        elif choice=="3":
            Search_Test()
        elif choice=="5":
            Delete_Test()
        elif choice=="6":
            print("Exiting the system...")
            login()
        else:
            print("Invalid Choice.Please try again.")

    while True:
        print("Clinical Management")
        success = login()
        if not success:
            print("Exiting the system")
            break


def main():
    if login()

main()