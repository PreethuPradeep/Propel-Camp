username="recept"
password="1234"
def login():
    uname=input("Username: ")
    pwd=input("Password: ")
    if uname==username and pwd==password:
        print("Login Successful!")
        return menu()
    
patients={}

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

def menu():
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
            break
        else:
            print("Invalid Choice.Please try again.")

if login():
    menu()
