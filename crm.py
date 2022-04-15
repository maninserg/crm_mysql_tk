from tkinter import *
import mysql.connector

root = Tk()

root.title("CRM System")
root.geometry("400x400")

# Connect to MySQL
mydb = mysql.connector.connect(
    host = "localhost",
    database = "crm",
    user = "crmuser",
    password = "123456"
)

# Check to see if connection to MySQL was created
# print(mydb)

# Create a cursor and initialize it
my_cursor = mydb.cursor()

# Create database
# my_cursor.execute("CREATE DATABASE crm")

# Test to see if database was created
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)

# Create a table
'''
my_cursor.execute("""CREATE TABLE customers (
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    zipcode INT(10),
    price_paid DECIMAL(10, 2),
    user_id INT AUTO_INCREMENT PRIMARY KEY
)""")
'''

# Show table
my_cursor.execute("SELECT * FROM customers")
for item in my_cursor.description:
    print(item)

root.mainloop()