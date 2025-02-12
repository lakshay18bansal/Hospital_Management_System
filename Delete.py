"""Deleting Records to MYSQL Database"""

# LOADING REQUIRED LIBRARIES
import mysql.connector as m
import tabulate

# Connecting to MYSQL server
file=m.connect(host='localhost',user='root',password="",database="HOSPITAL")
b=file.cursor()

# Deleting Records
def delete_record():
    print("1. Delete Doctor Records\n2. Delete Patient Records")
    ch=int(input("Enter Choice: "))
    if ch==1:
        print("1. Delete by Name\n2. Delete by ID")
        choice=int(input("Enter choice: "))
        if choice==1:
            name=input("Enter Doctor's Name: ")
            b.execute("select * from doctor where name='{}'".format(name))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t---------------NO SUCH RECORD FOUND!!!---------------")
            else:
                print("\t\t\t------------DOCTOR Records-------")
                for i in data:
                    print(tabulate.tabulate([i],headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
                    x=input("Press Y to delete this record: ")
                    if x.upper()=='Y':
                        b.execute("insert into restore_doctor values('{}','{}','{}','{}')".format(i[0],i[1],i[2],i[3]))
                        b.execute("delete from doctor where ID='{}'".format(i[1]))
                        print("\t\t\t---------RECORD DELETED--------")
                        file.commit()
                        break
        elif choice==2:
            ID=input("Enter Doctor's ID: ")
            b.execute("select * from doctor where id='{}'".format(ID))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t---------------NO SUCH RECORD FOUND!!!---------------")
            else:
                print("\t\t\t------------DOCTOR Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
                x=input("Press Y to delete this record: ")
                if x.upper()=='Y':
                    b.execute("insert into restore_doctor values('{}','{}','{}','{}')".format(data[0][0],data[0][1],data[0][2],data[0][3]))
                    b.execute("delete from doctor where ID='{}'".format(ID))
                    print("\t\t\t---------RECORD DELETED--------")
                    file.commit()
        else:
            print("\t\t----------INVALID INPUT!!--------")
    elif ch==2:
        print("1. Delete by Name\n2. Delete by ID")
        choice=int(input("Enter choice: "))
        if choice==1:
            name=input("Enter Patient's Name: ")
            b.execute("select * from patient where name='{}'".format(name))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t---------------NO SUCH RECORD FOUND!!!---------------")
            else:
                print("\t\t\t------------PATIENT Records-------")
                for i in data:
                    print(tabulate.tabulate([i],headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
                    x=int(input("Press Y to delete this record: "))
                    if x.upper()=='Y':
                        b.execute("insert into restore_patient values('{}','{}','{}','{}','{}')".format(i[0],i[1],i[2],i[3],i[4]))
                        b.execute("delete from doctor where ID='{}'".format(i[1]))
                        print("\t\t\t---------RECORD DELETED--------")
                        file.commit()
                        break
        elif choice==2:
            ID=input("Enter Patient's ID: ")
            b.execute("select * from Patient where id='{}'".format(ID))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t---------------NO SUCH RECORD FOUND!!!---------------")
            else:
                print("\t\t\t------------PATIENT Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
                x=input("Press Y to delete this record: ")
                if x.upper()=='Y':
                    b.execute("insert into restore_patient values('{}','{}','{}','{}','{}')".format(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4]))
                    b.execute("delete from patient where ID='{}'".format(ID))
                    print("\t\t\t---------RECORD DELETED--------")
                    file.commit()
        else:
            print("\t\t----------INVALID INPUT!!--------")
    else:
        print("\t\t----------INVALID INPUT!!--------")
