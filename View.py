"""Viewing Records to MYSQL Database"""

# LOADING REQUIRED LIBRARIES
import mysql.connector as m
import tabulate

# Connecting to MYSQL server
file=m.connect(host='localhost',user='root',password="",database="HOSPITAL")
b=file.cursor()

# Viewing Records
def view_record():
    print("1. View Doctor's Records\n2. View Patient Records")
    ch=int(input("Enter Choice: "))
    if ch==1:
        print("1. View All Records\n2. View Records in Alphabetical order")
        print("3. View Records in Increasing Doctor ID")
        print("4. View Records in Decreasing Doctor ID")
        choice=int(input("Enter choice: "))
        if choice==1:
            b.execute("select * from doctor")
            data=b.fetchall()
            if data==[]:
                print("\t\t----------NO RECORD FOUND!!  -------")
            else:
                print("\t\t------------DOCTOR Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
        elif choice==2:
            b.execute("select * from doctor order by Name")
            data=b.fetchall()
            if data==[]:
                print("\t\t----------NO RECORD FOUND!!-------")
            else:
                print("\t\t------------DOCTOR Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
        elif choice==3:
            b.execute("select * from doctor order by ID")
            data=b.fetchall()
            if data==[]:
                print("\t\t----------NO RECORD FOUND!!  -------")
            else:
                print("\t\t------------DOCTOR Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
        elif choice==4:
            b.execute("select * from doctor order by ID desc")
            data=b.fetchall()
            if data==[]:
                print("\t\t----------NO RECORD FOUND!!  -------")
            else:
                print("\t\t------------DOCTOR Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
        else:
            print("\t\t----------INVALID INPUT!!--------")
    elif ch==2:
        print("1. View All Records\n2. View Records in Alphabetical order")
        print("3. View Records in Increasing Patient ID")
        print("4. View Records in Decreasing Patient ID")
        choice=int(input("Enter choice: "))
        if choice==1:
            b.execute("select * from patient")
            data=b.fetchall()
            if data==[]:
                print("\t\t----------NO RECORD FOUND!!  -------")
            else:
                print("\t\t------------PATIENT Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
        elif choice==2:
            b.execute("select * from patient order by Name")
            data=b.fetchall()
            if data==[]:
                print("\t\t----------NO RECORD FOUND!!-------")
            else:
                print("\t\t------------PATIENT Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
        elif choice==3:
            b.execute("select * from patient order by ID")
            data=b.fetchall()
            if data==[]:
                print("\t\t----------NO RECORD FOUND!!  -------")
            else:
                print("\t\t------------PATIENT Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
        elif choice==4:
            b.execute("select * from patient order by ID desc")
            data=b.fetchall()
            if data==[]:
                print("\t\t----------NO RECORD FOUND!!  -------")
            else:
                print("\t\t------------PATIENT Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
        else:
            print("\t\t----------INVALID INPUT!!--------")
    else:
        print("\t\t----------INVALID INPUT!!--------")
