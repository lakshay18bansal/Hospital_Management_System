"""Restoring Records to MYSQL Database"""

# LOADING REQUIRED LIBRARIES
import mysql.connector as m
import tabulate

# Connecting to MYSQL server
file=m.connect(host='localhost',user='root',password="",database="HOSPITAL")
b=file.cursor()

# Restoring Records
def restore_record():
    print("1. Restore Doctor Records\n2. Restore Patient Records")
    ch=int(input("Enter Choice: "))
    if ch==1:
        print("1. Restore Using Name\n2. Restore using ID")
        choice=int(input("Enter Choice: "))
        if choice==1:
            name=input("Enter Name: ")
            b.execute("select * from restore_doctor where name='{}'".format(name))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t----------NO SUCH RECORD DELETED---------")
            else:
                for i in data:
                    print(tabulate.tabulate([i],headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
                    x=input("ENTER Y to  restore this data: ")
                    if x.upper()=='Y':
                        b.execute("insert into doctor values('{}','{}','{}','{}')".format(i[0],i[1],i[2],i[3]))
                        b.execute("delete from restore_doctor where ID='{}'".format(i[1]))
                        file.commit()
                        print("\t\t\t-----------THIS RECORD IS SUCCESSFULLY RESTORED---------")
                        break
        elif choice==2:
            ID=int(input("Enter ID: "))
            b.execute("select * from restore_doctor where ID='{}'".format(ID))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t----------NO SUCH RECORD DELETED---------")
            else:
                print(tabulate.tabulate(data,headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
                x=input("ENTER Y to  restore this data: ")
                if x.upper()=='Y':
                    b.execute("insert into doctor values('{}','{}','{}','{}')".format(data[0][0],data[0][1],data[0][2],data[0][3]))
                    b.execute("delete from restore_doctor where ID='{}'".format(ID))
                    file.commit()
                    print("\t\t\t-----------THIS RECORD IS SUCCESSFULLY RESTORED---------")
        else:
            print("\t\t\t-----------INVALID INPUT--------------")
    elif ch==2:
        print("1. Restore Using Name\n2. Restore using ID")
        choice=int(input("Enter Choice: "))
        if choice==1:
            name=input("Enter Name: ")
            b.execute("select * from restore_patient where name='{}'".format(name))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t----------NO SUCH RECORD DELETED---------")
            else:
                for i in data:
                    print(tabulate.tabulate([i],headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
                    x=input("ENTER Y to  restore this data: ")
                    if x.upper()=='Y':
                        b.execute("insert into patient values('{}','{}','{}','{}','{}')".format(i[0],i[1],i[2],i[3],i[4]))
                        b.execute("delete from restore_patient where ID='{}'".format(i[1]))
                        file.commit()
                        print("\t\t\t-----------THIS RECORD IS SUCCESSFULLY RESTORED---------")
                        break
        elif choice==2:
            ID=int(input("Enter ID: "))
            b.execute("select * from restore_patient where ID='{}'".format(ID))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t----------NO SUCH RECORD DELETED---------")
            else:
                print(tabulate.tabulate(data,headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
                x=input("ENTER Y to  restore this data: ")
                if x.upper()=='Y':
                    b.execute("insert into patient values('{}','{}','{}','{}','{}')".format(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4]))
                    b.execute("delete from restore_patient where ID='{}'".format(ID))
                    file.commit()
                    print("\t\t\t-----------THIS RECORD IS SUCCESSFULLY RESTORED---------")
        else:
            print("\t\t\t-----------INVALID INPUT--------------")
    else:
        print("\t\t\t-------------INVALID CHOICE----------")
