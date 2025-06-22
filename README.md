# Hospital Management System (Standalone Scripts)

A simple, script-based Hospital Management System in Python that performs record management operations such as Add, Delete, Update, View, Search, Export, and Restore using a MySQL database.

---

## 🧾 Overview

This project provides basic patient record management through standalone Python scripts. Each operation is encapsulated in a separate file, making it easy to understand and modify. Data is stored and managed via a MySQL backend.

---

## 📁 Files Overview

| File                  | Description                            |
|-----------------------|----------------------------------------|
| `Add.py`              | Adds new hospital/patient records      |
| `Delete.py`           | Deletes existing records               |
| `Update.py`           | Updates record details                 |
| `View.py`             | Displays all stored records            |
| `Search.py`           | Searches for records by criteria       |
| `Export.py`           | Exports records to MySQL database      |
| `Restore.py`          | Restores records from the database     |
| `HOSPITAL_MANAGEMENT.py` | Entry point to run all functions       |

---

## 💾 Prerequisites

- Python 3.x
- `mysql-connector-python`
- MySQL server installed and running

Install dependencies:
 
pip install mysql-connector-python
 

---


## 🚀 How to Run

Make sure MySQL server is running and credentials are set inside the relevant scripts.

Run operations individually:


python Add.py         # To add records
python View.py        # To view records
python Search.py      # To search records
python Update.py      # To update records
python Delete.py      # To delete records
python Export.py      # To export data to DB
python Restore.py     # To restore data from DB

--- 

Or use the sample runner:
python HOSPITAL_MANAGEMENT.py


## 🧠 Features
- Basic CRUD operations on patient records
- MySQL database integration
- Modular structure with one function per script
- Easy to extend and customize

---




