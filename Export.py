"""Exporting Records to MYSQL Database"""

# LOADING REQUIRED LIBRARIES
import mysql.connector as m
import tabulate

# Connecting to MYSQL server
file=m.connect(host='localhost',user='root',password="",database="HOSPITAL")
b=file.cursor()

# Exporting Records
def export_record():
    print("1. Export Doctor Details\n2. Export Patient Details")
    import csv
    ch=int(input("Enter Choice: "))
    if ch==1:
        x=input("Enter Name of file: ")
        y='C:\\Users\\LAKSHAY\\OneDrive\\Desktop\\PYTHON Programs\\Usersfiles\\'+x+'.csv'
        try:
            f=open(y)
            print("\t\t\t----------THIS FILE NAME IS ALREADY PRESENT!!-------------")
            print("\t\t\t-------------------PLEASE TRY AGAIN!!---------------")
        except:
            f=open(y,'w',newline='')
            b.execute("select * from Doctor")
            data=b.fetchall()
            data1=csv.writer(f)
            data1.writerows(data)
            print("Your file Has been Created at location: ",y)
            f.close()
    elif ch==2:
        x=input("Enter Name of file: ")
        y='C:\\Users\\LAKSHAY\\OneDrive\\Desktop\\PYTHON Programs\\Usersfiles\\'+x+'.csv'
        try:
            f=open(y)
            print("\t\t\t----------THIS FILE NAME IS ALREADY PRESENT!!-------------")
            print("\t\t\t-------------------PLEASE TRY AGAIN!!---------------")
        except:
            f=open(y,'w',newline='')
            b.execute("select * from Patient")
            data=b.fetchall()
            data1=csv.writer(f)
            data1.writerows(data)
            print("Your file Has been Created at location: ",y)
            f.close()
    else:
        print("\t\t\t-------------INVALID INPUT!!!!------------------")
