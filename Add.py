"""Adding Records to MYSQL Database"""

# LOADING REQUIRED LIBRARIES
import mysql.connector as m
import tabulate

# Connecting to MYSQL server
file=m.connect(host='localhost',user='root',password="",database="HOSPITAL")
b=file.cursor()

# Adding record
def add_record():
    print("1. Add DOCTOR's details\n2. Add Patient details")
    ch=int(input("Enter Choice: "))
    if ch==1:
        y=int(input("Enter ID: "))
        b.execute("select * from doctor where ID='{}'".format(y))
        data=b.fetchall()
        if data==[]:
            name=input("Enter name: ")
            q=int(input("Enter Salary: "))
            p=input("Enter Specialization: ")
            b.execute("insert into doctor values('{}','{}','{}','{}')".format(name,y,q,p))
            file.commit()
            print("\t\t-------------------RECORD ADDED SUCCESSFULLY----------------")
        else:
            print("\t\t------------ID ALREADY EXISTS-----------")
    elif ch==2:
        y=int(input("Enter ID: "))
        b.execute("select * from patient where ID='{}'".format(y))
        data=b.fetchall()
        if data==[]:
            name=input("Enter name: ")
            disease=input("Enter disease: ")
            date=input("Enter Admission date: ")
            address=input("Enter Address: ")
            b.execute("insert into patient values('{}','{}','{}','{}','{}')".format(name,y,disease,date,address))
            file.commit()
            print("\t\t-------------------RECORD ADDED SUCCESSFULLY----------------")
        else:
            print("\t\t------------ID ALREADY EXISTS-----------")