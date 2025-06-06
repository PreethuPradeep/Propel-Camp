#Clinic Management System
##  `clinic-management-system/README.md`

---

#  Clinic Management System

A command-line Clinic Management System with multiple user roles (Admin, Receptionist, Pharmacist, Lab Technician), each able to manage different parts of clinic data using Python dictionaries and functions.

---

##  Roles & Responsibilities

###  Admin:
- Add/View/Update/Delete staff records

###  Receptionist:
- Add/View/Update/Delete patient records

###  Pharmacist:
- Add/View/Update/Delete medicine details

###  Lab Technician:
- Add/View/Update/Delete test details

---

##  Data Entities

- Staff: `staff_id`, `name`, `designation`, `joining_date`, `salary`, `location`, etc.
- Patients: `patient_id`, `name`, `age`, `disease`, `blood_group`, etc.
- Medicines: `medicine_id`, `name`, `generic_name`, `company_name`, `price`
- Lab Tests: `test_id`, `test_name`, `range`, `price`

---

##  Login Access

Each role has a predefined username and password (can be hardcoded for now). Upon login, the system presents role-specific options.

---

## 🧪 How to Run

```bash
python main.py


---
