# MySQL Connectivity with Python

import mysql.connector

def insert(myDB, myCursor, values):
    query = "INSERT INTO students VALUES(%s, %s, %s)"
    myCursor.execute(query, values)
    myDB.commit()


def update(myDB, myCursor, values):
    query = "UPDATE students SET roll_no=%s, name=%s, marks=%s WHERE roll_no = %s"
    myCursor.execute(query, values)
    if myCursor.rowcount == 0:
        print(" No Such Record!!")
        return False

    myDB.commit()
    return True


def delete(myDB, myCursor, values):
    query = "DELETE FROM students WHERE roll_no = %s"
    myCursor.execute(query, values)
    if myCursor.rowcount == 0:
        print(" No Such Record!!")
        return False
    
    myDB.commit()
    return True


def display(myCursor):
    query = "SELECT * FROM Students"
    myCursor.execute(query)
    for itr in myCursor:
        print(f'\t {itr}')


def main():
    myDB = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "password",
        database = "COMPUTER_DEPT"
    )
    print(f' \n Successfully Connected to --> {myDB}')
    myCursor = myDB.cursor()
    
    choice = 1
    while True:
        print("\n Choose from the following --> ")
        print(" 1. Insert \n 2. Update \n 3. Delete \n 4. Display \n 5. Exit")
        choice = int(input())
        if choice == 1:
            rollNo = int(input('\t Enter Roll Number : '))
            name = input('\t Enter the Name : ')
            marks = int(input('\t Enter the Marks : '))

            insert(myDB, myCursor, (rollNo, name, marks))
            print(" Record Inserted Successfully!")
        
        elif choice == 2:
            targetRollNo = int(input("\t Enter RollNo of student to Update : "))
            rollNo = int(input('\t Enter new RollNo : '))
            name = input('\t Enter new Name : ')
            marks = int(input('\t Enter new Marks : '))

            if update(myDB, myCursor, (rollNo, name, marks, targetRollNo)):
                print(" Record Updated Successfully!")
        
        elif choice == 3:
            targetRollNo = int(input("\t Enter RollNo of student to Delete : "))
            if delete(myDB, myCursor, (targetRollNo, )):
                print(" Record Deleted Successfully!")
        
        elif choice == 4:
            print("<******* Data of the table : Students *******> ")
            display(myCursor)
        
        else:
            break
    
    print("Connection Reset Successfully!")
    myDB.close()


main()