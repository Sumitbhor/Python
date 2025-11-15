import mysql.connector

# Step 1: Connect to MySQL Database
connection = mysql.connector.connect(
    host="localhost",
    user="root",           # use your MySQL username
    password="root123",  # use your MySQL password
    database="college"      # use your database name
)

cursor = connection.cursor()



cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()

print("Student Records:")
for row in rows:
    print(row)

# Step 5: Close Connection
cursor.close()
connection.close()
