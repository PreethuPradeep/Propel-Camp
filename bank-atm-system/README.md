#Bank Atm System
##  `bank-atm-system/README.md`
---
#  Bank ATM System

A command-line Bank Management System simulating basic ATM and administrative banking features. Includes customer registration, transaction handling, and validation using Python.

---

##  Admin Features

- Add a new customer (auto-generate account number and ATM PIN)
- Update customer mobile/email
- Delete customer by account number
- View all customers
- View a specific customer's details

---

##  Customer Features

- Deposit money (PAN required if > ₹50,000)
- Withdraw money (check against available balance)
- View balance
- Transfer money to another account

---

##  Data Fields

Each customer includes:
- `Account Number` (9-digit, auto-generated)
- `Name`, `Account Type`, `Balance`, `Min Balance`
- `Mobile`, `Email`, `ATM PIN` (4-digit, auto-generated)

---

##  Validations

- Account numbers = 9 digits
- Mobile = 10 digits only
- PAN required for high-value transactions
- Error message for invalid or missing data

---

##  How to Run

```bash
python main.py
