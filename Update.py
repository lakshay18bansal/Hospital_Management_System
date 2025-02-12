"""UPDATING Records to MYSQL Database"""

# LOADING REQUIRED LIBRARIES
import mysql.connector as m
import tabulate

# Connecting to MYSQL server
file=m.connect(host='localhost',user='root',password="",database="HOSPITAL")
b=file.cursor()

# UPDATING Records
def update_record():
    print("1. Update Doctor details\n2. Update Patient Details")
    ch=int(input("Enter Choice: "))
    if ch==1:
        print("1. Find record using Doctor's name\n2. Find record using Doctor's ID")
        choice=int(input("Enter choice: "))
        if choice==1:
            name=input("Enter Name: ")
            b.execute("select * from doctor where Name='{}'".format(name))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t----------NO RECORD FOUND!!  -------")
            else:
                for i in data:
                    print(tabulate.tabulate([i],headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
                    c=input("Press Y to alter this record: ")
                    if c.upper()=='Y':
                        print("1. Update Name\n2. Update ID\n3. Update All details")
                        d=int(input("Enter choice:"))
                        if d==1:
                            n=input("Enter New Name: ")
                            b.execute("update doctor set Name='{}' where ID='{}'".format(n,i[1]))
                            print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                            file.commit()
                            break
                        elif d==2:
                            n=input("Enter New ID: ")
                            b.execute("select * from doctor where ID='{}'".format(n))
                            data1=b.fetchall()
                            if data1==[]:
                                b.execute("update doctor set ID='{}' where ID='{}'".format(n,i[1]))
                                print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                                file.commit()
                                break
                            else:
                                print("\t\t\t-----------THIS ID ALREADY EXISTS!!!!!-----------------")
                                print("\t\t\t---------PLEASE TRY AGAIN-------------")
                        elif d==3:
                            m=input("Enter New Name: ")
                            n=int(input("Enter New ID: "))
                            o=int(input("Enter New salary: "))
                            p=input("Enter New Specialization: ")
                            b.execute("update doctor set Name='{}',ID='{}',salary='{}',Specialization='{}' where ID='{}'".format(m,n,o,p,i[1]))
                            print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                            file.commit()
                            break
                        else:
                            print("\t\t\t----------INVALID INPUT--------")
        elif choice==2:
            ID=input("Enter ID: ")
            b.execute("select * from doctor where ID='{}'".format(ID))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t----------NO RECORD FOUND!!  -------")
            else:
                for i in data:
                    print(tabulate.tabulate([i],headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
                    c=input("Press Y to alter this record: ")
                    if c.upper()=='Y':
                        print("1. Update Name\n2. Update ID\n3. Update All details")
                        d=int(input("Enter choice:"))
                        if d==1:
                            n=input("Enter New Name: ")
                            b.execute("update doctor set Name='{}' where ID='{}'".format(n,i[1]))
                            print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                            file.commit()
                            break
                        elif d==2:
                            n=input("Enter New ID: ")
                            b.execute("select * from doctor where ID='{}'".format(n))
                            data1=b.fetchall()
                            if data1==[]:
                                b.execute("update doctor set ID='{}' where ID='{}'".format(n,i[1]))
                                print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                                file.commit()
                                break
                            else:
                                print("\t\t\t-----------THIS ID ALREADY EXISTS!!!!!-----------------")
                                print("\t\t\t---------PLEASE TRY AGAIN-------------")
                        elif d==3:
                            m=input("Enter New Name: ")
                            n=int(input("Enter New ID: "))
                            o=int(input("Enter New salary: "))
                            p=input("Enter New Specialization: ")
                            b.execute("update doctor set Name='{}',ID='{}',salary='{}',Specialization='{}' where ID='{}'".format(m,n,o,p,i[1]))
                            print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                            file.commit
                            break
                        else:
                            print("\t\t\t----------INVALID INPUT--------")
    elif ch==2:
        print("1. Find record using Patient's name\n2. Find record using Patient's ID")
        choice=int(input("Enter choice: "))
        if choice==1:
            name=input("Enter Name: ")
            b.execute("select * from patient where Name='{}'".format(name))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t----------NO RECORD FOUND!!  -------")
            else:
                for i in data:
                    print(tabulate.tabulate([i],headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
                    c=input("Press Y to alter this record: ")
                    if c.upper()=='Y':
                        print("1. Update Name\n2. Update ID\n3. Update All details")
                        d=int(input("Enter choice:"))
                        if d==1:
                            n=input("Enter New Name: ")
                            b.execute("update patient set Name='{}' where ID='{}'".format(n,i[1]))
                            print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                            file.commit()
                            break
                        elif d==2:
                            n=input("Enter New ID: ")
                            b.execute("select * from patient where ID='{}'".format(n))
                            data1=b.fetchall()
                            if data1==[]:
                                b.execute("update patient set ID='{}' where ID='{}'".format(n,i[1]))
                                print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                                file.commit()
                                break
                            else:
                                print("\t\t\t-----------THIS ID ALREADY EXISTS!!!!!-----------------")
                                print("\t\t\t---------PLEASE TRY AGAIN-------------")
                        elif d==3:
                            m=input("Enter New Name: ")
                            n=int(input("Enter New ID: "))
                            o=input("Enter Disease: ")
                            p=input("Enter New Date_of_admission: ")
                            q=input("Enter New Address: ")
                            b.execute("update patient set Name='{}',ID='{}',Disease='{}',Date_Admitted='{}',Address='{}' where ID='{}'".format(m,n,o,p,q,i[1]))
                            print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                            file.commit()
                            break
                        else:
                            print("\t\t\t----------INVALID INPUT--------")
        elif choice==2:
            ID=input("Enter ID: ")
            b.execute("select * from patient where ID='{}'".format(ID))
            data=b.fetchall()
            if data==[]:
                print("\t\t----------NO RECORD FOUND!!  -------")
            else:
                for i in data:
                    print(tabulate.tabulate([i],headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
                    c=input("Press Y to alter this record: ")
                    if c.upper()=='Y':
                        print("1. Update Name\n2. Update ID\n3. Update All details")
                        d=int(input("Enter choice:"))
                        if d==1:
                            n=input("Enter New Name: ")
                            b.execute("update patient set Name='{}' where ID='{}'".format(n,i[1]))
                            print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                            file.commit()
                            break
                        elif d==2:
                            n=input("Enter New ID: ")
                            b.execute("select * from patient where ID='{}'".format(n))
                            data1=b.fetchall()
                            if data1==[]:
                                b.execute("update patient set ID='{}' where ID='{}'".format(n,i[1]))
                                print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                                file.commit()
                                break
                            else:
                                print("\t\t\t-----------THIS ID ALREADY EXISTS!!!!!-----------------")
                                print("\t\t\t---------PLEASE TRY AGAIN-------------")
                        elif d==3:
                            m=input("Enter New Name: ")
                            n=int(input("Enter New ID: "))
                            o=input("Enter Disease: ")
                            p=input("Enter New Date_of_admission: ")
                            q=input("Enter New Address: ")
                            b.execute("update patient set Name='{}',ID='{}',Disease='{}',Date_Admitted='{}',Address='{}' where ID='{}'".format(m,n,o,p,q,i[1]))
                            print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                            file.commit()
                            break
                        else:
                            print("\t\t----------INVALID INPUT--------")
        else:
            print("\t\t----------INVALID INPUT--------")
    else:
        print("\t\t----------INVALID CHOICE--------")    
