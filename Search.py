"""Searching Records to MYSQL Database"""

# LOADING REQUIRED LIBRARIES
import mysql.connector as m
import tabulate

# Connecting to MYSQL server
file=m.connect(host='localhost',user='root',password="",database="HOSPITAL")
b=file.cursor()

# Searching Records
def search_record():
    print("1. Search DOCTOR Details\n2. Search Patient Details")
    ch=int(input("Enter Choice: "))
    if ch==1:
        print("1. Search by Name\n2. Search by ID")
        choice=int(input("Enter choice: "))
        if choice==1:
            name=input("Enter Doctor's Name: ")
            b.execute("select * from doctor where name='{}'".format(name))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t---------------NO SUCH RECORD FOUND!!!---------------")
            else:
                print("\t\t\t------------DOCTOR Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
        elif choice==2:
            ID=input("Enter Doctor's ID: ")
            b.execute("select * from doctor where id='{}'".format(ID))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t---------------NO SUCH RECORD FOUND!!!---------------")
            else:
                print("\t\t\t------------DOCTOR Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
        else:
            print("\t\t----------INVALID INPUT!!!--------")
    elif ch==2:
        print("1. Search by Name\n2. Search by ID")
        choice=int(input("Enter choice: "))
        if choice==1:
            name=input("Enter Patient's Name: ")
            b.execute("select * from patient where name='{}'".format(name))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t---------------NO SUCH RECORD FOUND!!!---------------")
            else:
                print("\t\t\t------------Patient Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
        elif choice==2:
            ID=input("Enter Patient's ID: ")
            b.execute("select * from patient where id='{}'".format(ID))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t---------------NO SUCH RECORD FOUND!!!---------------")
            else:
                print("\t\t\t------------PATIENT Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
        else:
            print("\t\t----------INVALID INPUT!!!--------")
    else:
        print("\t\t----------INVALID INPUT!!!--------")