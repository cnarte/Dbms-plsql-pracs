import pymongo

def insert(myCollection, custID, name, address, age):
    document = {
        "CustID" : custID,
        "Name" : name,
        "Address" : address,
        "Age" : age
    }
    myCollection.insert_one(document)


def delete(myCollection, CustID):
    query = {"CustID" : CustID}
    myCollection.delete_one(query)
    

def update(myCollection, custID, name, address, age):
    query = {"CustID": {"$eq": custID}}
    new_values = {'$set': {"Name": name, "Address" : address, "Age" : age}}
    myCollection.update_one(query, new_values)


def display(myCollection):
    for document in myCollection.find():
        print(document)


def main():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    myDB = client["Restaurant"]
    #print(client.list_database_names())

    myCollection = myDB["Customers"]

    choice = 1
    while True:
        print("\n Choose from the following --> ")
        print(" 1. Insert \t 2. Delete \t 3. Update \t 4. Display \t 5. Exit")
        choice = int(input())
        if choice == 1:
            custID = int(input('\t Enter Cutomer ID : '))
            name = input('\t Enter the Name : ')
            address = input('\t Enter the Address : ')
            age = int(input('\t Enter the Age : '))

            insert(myCollection, custID, name, address, age)
            print('Document Inserted Successfully')

        elif choice == 2:
            custID = int(input('\t Enter Cutomer ID  to delete: '))
            delete(myCollection, custID)
            print('Document Deleted Successfully')
   
        elif choice == 3:
            custID = int(input('\t Enter Cutomer ID to Update: '))
            name = input('\t Enter new Name : ')
            address = input('\t Enter new Address : ')
            age = int(input('\t Enter new Age : '))

            update(myCollection, custID, name, address, age)
            print('Document Updated Successfully')

        elif choice == 4:
            print("<---- Documents in the Customers ---->")
            display(myCollection)

        else:
            break
    

main()