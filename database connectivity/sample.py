import mysql.connector
# Connect to MySQL
dbConnection = mysql.connector.connect(host="localhost", user="root",  password="Root123", database="Product_db")

print("hello from out")

dbCommand = dbConnection.cursor()

def  get_product():
    dbCommand.execute("SELECT * FROM product")
    result = dbCommand.fetchall()
    for row in result:
        print(row)


# DELETE
def delete_product():
    id = int(input("Enter product_id: "))
    sql = "DELETE FROM product WHERE product_id=%s"   #Query
    dbCommand.execute(sql, (id,))
    dbConnection.commit()
    print("product deleted successfully")


# CREATE
def add_product():
   
    name = input("Enter product_name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter Price: "))

    sql = "INSERT INTO product ( product_name, quantity, price) VALUES ( %s, %s, %s)"
    values = ( name, quantity, price)

    dbCommand.execute(sql, values)
    dbConnection.commit()
    print("product added successfully")


# UPDATE
def update_product():
    id = int(input("Enter product_id: "))
    name = input("Enter new name: ")
    quantity = int(input("Enter new quantity: "))
    price = float(input("Enter new price: "))

    sql = "UPDATE product SET product_name=%s, quantity=%s, price=%s WHERE product_id=%s"
    values = (name, quantity, price, id)

    dbCommand.execute(sql, values)
    dbConnection.commit()

    print("product updated successfully")


#menu


    print("hello from while loop")
while 1:
    print("\n1. Add product")
    print("2. Show products")
    print("3. Update product")
    print("4. Delete product")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        get_product()

    elif choice == "3":
        update_product()

    elif choice == "4":
        delete_product()

    elif choice == "5":
        break

    else:
        print("Invalid choice")

dbCommand.close()
dbConnection.close()



# Data Layer: MySQL database connection 
#             Creating database, inerting sample data,
#             Testing database using SQL commands, Join queires and Stored procedure 
#             from the prespective of DBA

# DAL "Data Access Layer"
#            from the perspective of a developer,
#            we will create a python application to connect to the database and
#            perform CRUD operations on the database.