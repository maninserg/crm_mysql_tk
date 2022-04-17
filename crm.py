from tkinter import *
import mysql.connector
import csv 

root = Tk()

root.title("CRM System")
root.geometry("400x600")

# Connect to MySQL
mydb = mysql.connector.connect(
    host = "localhost",
    database = "crm",
    user = "crmuser",
    password = "123456"
)

# Check to see if connection to MySQL was created
print(mydb)

# Create a cursor and initialize it
my_cursor = mydb.cursor(buffered=True)

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

# Alter Table
'''
my_cursor.execute(""" ALTER TABLE customers ADD (
    email VARCHAR(255),
    address_1 VARCHAR(255),
    address_2 VARCHAR(255),
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(255),
    phone VARCHAR(255),
    payment_method VARCHAR(50),
    discount_code VARCHAR(255))
""")
'''

# Delete Table
'''
my_cursor.execute("DROP TABLE customers")
'''

# Show table
my_cursor.execute("SELECT * FROM customers")
for item in my_cursor.description:
    print(item)


# Clear Text Fields
def clear_fields():
    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    address1_box.delete(0, END)
    address2_box.delete(0, END)
    city_box.delete(0, END)
    state_box.delete(0, END)
    zipcode_box.delete(0, END)
    country_box.delete(0, END)
    phone_box.delete(0, END)
    email_box.delete(0, END)
    payment_method_box.delete(0, END)
    discount_code_box.delete(0, END)
    price_paid_box.delete(0, END)

# Submit Customer To DataBase
def add_customer():
    sql_command = "INSERT INTO customers (first_name, last_name, zipcode, price_paid, email, address_1, address_2, city, state, country, phone, payment_method, discount_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (first_name_box.get(), last_name_box.get(), zipcode_box.get(), price_paid_box.get(),
              email_box.get(), address1_box.get(), address2_box.get(), city_box.get(), state_box.get(),
              country_box.get(), phone_box.get(), payment_method_box.get(), discount_code_box.get()) 
    my_cursor.execute(sql_command, values)

    # Commit the changes to the database
    mydb.commit()
    # Clear fields 
    clear_fields()

# Write List Customers to csv file
def write_to_csv(result):
    with open('customers.csv', 'a') as f:
        w = csv.writer(f, dialect='excel')
        w.writerows(result)

# List Customers
def list_customers():
    list_customers_query = Tk()
    list_customers_query.title("List All Customers")
    list_customers_query.geometry("800x600")
    # Query The Database
    my_cursor.execute("SELECT * FROM customers")
    result = my_cursor.fetchall()
    for index, item in enumerate(result):
        num = 0
        for field in item:
            lookup_label = Label(list_customers_query, text=field)
            lookup_label.grid(row=index, column=num)
            num += 1
    csv_button = Button(list_customers_query, text="Save to Excel", command=lambda: write_to_csv(result))
    csv_button.grid(row=index+1, column=0)


# Create a label
title_label = Label(root, text="My Customer Database", font=("Helvetica"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Create Main Form To Enter Cusmomer Data
first_name_label = Label(root, text="First name").grid(row=1, column=0, sticky=W, padx=10)
last_name_label = Label(root, text="Last name").grid(row=2, column=0, sticky=W, padx=10)
address1_label = Label(root, text="Address 1").grid(row=3, column=0, sticky=W, padx=10)
address2_label = Label(root, text="Address 2").grid(row=4, column=0, sticky=W, padx=10)
city_label = Label(root, text="City").grid(row=5, column=0, sticky=W, padx=10)
state_label = Label(root, text="State").grid(row=6, column=0, sticky=W, padx=10)
zipcode_label = Label(root, text="ZipCode").grid(row=7, column=0, sticky=W, padx=10)
country_label = Label(root, text="Country").grid(row=8, column=0, sticky=W, padx=10)
phone_label = Label(root, text="Phone").grid(row=9, column=0, sticky=W, padx=10)
email_label = Label(root, text="Email").grid(row=10, column=0, sticky=W, padx=10)
payment_method_label = Label(root, text="Payment Method").grid(row=11, column=0, sticky=W, padx=10)
dicount_code_label = Label(root, text="Discount Code").grid(row=12, column=0, sticky=W, padx=10)
price_paid_label = Label(root, text="Price Paid").grid(row=13, column=0, sticky=W, padx=10)

# Create entry boxes
first_name_box = Entry(root)
first_name_box.grid(row=1, column=1, pady=5)

last_name_box = Entry(root)
last_name_box.grid(row=2, column=1, pady=5)

address1_box = Entry(root)
address1_box.grid(row=3, column=1, pady=5)

address2_box = Entry(root)
address2_box.grid(row=4, column=1, pady=5)

city_box = Entry(root)
city_box.grid(row=5, column=1, pady=5)

state_box = Entry(root)
state_box.grid(row=6, column=1, pady=5)

zipcode_box = Entry(root)
zipcode_box.grid(row=7, column=1, pady=5)

country_box = Entry(root)
country_box.grid(row=8, column=1, pady=5)

phone_box = Entry(root)
phone_box.grid(row=9, column=1, pady=5)

email_box = Entry(root)
email_box.grid(row=10, column=1, pady=5)

payment_method_box = Entry(root)
payment_method_box.grid(row=11, column=1, pady=5)

discount_code_box = Entry(root)
discount_code_box.grid(row=12, column=1, pady=5)

price_paid_box = Entry(root)
price_paid_box.grid(row=13, column=1, pady=5)

# Create Buttons
add_customer_button = Button(root, text="Add Customer To DataBase", command=add_customer)
add_customer_button.grid(row=14, column=0, padx=10, pady=10)

clear_fields_button = Button(root, text="Clear Fields", command=clear_fields)
clear_fields_button.grid(row=14, column=1)

# List customers button
list_customers_button = Button(root, text="List Customers", command=list_customers)
list_customers_button.grid(row=15, column=0, sticky=W, padx=10)

# Print All Items from customers table
my_cursor.execute("SELECT * FROM customers")
result = my_cursor.fetchall()
for item in result:
    print(item)


root.mainloop()