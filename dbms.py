import sqlite3

db_conn = sqlite3.connect('College_addmission.db')
mycursor = db_conn.cursor()
mycursor.execute("""CREATE TABLE IF NOT EXISTS MAJOR_INFO(Addmission_no integer,
  Student_Name varchar(20),
  Major_name varchar(30),
  Date_Of_Birth varchar(20),
  Gaurdian_Name varchar(20),
  Contact_no integer,
  Email varchar(40),
  Usage_of_Dorm varchar(5),
  Fees_to_be_payed float(10,5))""")
print("Table Created!")

def Menue():
    print("*"*80)
    print("\t\t MAIN MENU\n")
    print("\t 1. Add student details")
    print("\t 2. Display the details")
    print("\t 3. Update fees")
    print("\t 4. Delete a detail")
    print("*"*80)
    print()

def add_data():
  ans='y'
  while ans in 'Yy':
    ad_no= int(input("Enter the admission number: "))
    st_name= input("Enter the name of the student: ")
    major= input("Enter the major: ")
    dob= (input("Enter the Date Of Birth: "))
    g_name= input("Enter the Gaurdian's name: ")
    c_no= int(input("Enter the contact number: "))
    email=input("Enter the email: ")
    dorm= input(" Usage of dorm Y/N: ")
    fee= float(input("Enter the fees you have paid: "))
    mycursor.execute("INSERT INTO MAJOR_INFO VALUES({},'{}','{}','{}','{}',{},'{}','{}',{})".format(ad_no,st_name,major,dob,g_name,c_no,email,dorm,fee))
    print("Row inserted")
    db_conn.commit()
    ans=input("Do you want to enter more records Y/N:")

def display():
  mycursor.execute("SELECT * FROM MAJOR_INFO")
  records = mycursor.fetchall() 
  print("Admission number\tStudent Name\t\t\tMajor Name\t\t\t\tDOB\t\t\tGuardian's Name\t\t\tContact Number\t\t\t\t\tEmail\t\t\tDorm Status\t\tFee To Be Paid")
  for row in records:
    for i in row:
      print(i, end="\t\t\t")
    print("\n")

def modify():
  st_name=input("Enter Student Name:")
  Fee_change="Update MAJOR_INFO set Fees_to_be_payed=Fees_to_be_payed-50000 where Student_Name=?"
  mycursor.execute(Fee_change,(st_name,))
  db_conn.commit()
  print(Fee_change)

def del_record():
  ad_no=int(input("Enter Addmission no of the student whose record is to be deleted:"))
  Drop_st="Delete from MAJOR_INFO where Addmission_no= '%ad_no' "
  mycursor.execute(Drop_st)
  db_conn.commit()
  print("This student has dropped")

#main
Menue()
opt='y'
while opt in 'Yy':
  choice=int(input("Enter your choice:"))
  if choice==1:
    add_data()
  elif choice==2:
    display()
  elif choice==3:
    modify()
  elif choice==4:
    del_record()
  else:
    print("Invalid choice")
  opt=input("Return to Main Menu Y/N:")
db_conn.close()

