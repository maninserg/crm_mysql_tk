from tkinter import *
import mysql.connector

root = Tk()

root.title("CRM System")
root.geometry("400x400")

mydb = mysql.connector.connect(
    host = "localhost",
    database = "crm",
    user = "crmuser",
    password = "123456"
)

print(mydb)

root.mainloop()