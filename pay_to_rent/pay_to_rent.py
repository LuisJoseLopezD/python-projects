from tkinter import ttk
from tkinter import *
import tkinter as tk
import sqlite3
from sqlite3 import Error
 

#2ST WINDOW

def add():
    root = tk.Tk()
    root.title("Add Resident")
    root.geometry("400x250") #Geometry
    root.config(bg="white")

    def add_exit():
        root.destroy()

    def addsuccesfully():
        display = tk.Label(root, text="Resident added succesfully")
        display.grid(row=6,column=1,columnspan=2)
        display.config(bg="white", fg="blue")

    def addresident():
        database = 'database.db'  
        conn = sqlite3.connect(database) #Connect database
        name1 = str(name.get())
        cedula1 = int(cedula.get())
        phone1 = int(phone.get())
        mod1 = str(mod.get())
        status1 = str(status.get())
        params = (name1, cedula1, phone1, mod1, status1)
        cur = conn.cursor()
        new = test_table.get_children() #CLEANING TABLE
        for element in new:
            test_table.delete(element)
        cur.execute("INSERT INTO test_table VALUES(?, ?, ?, ?, ?)", params) #INSERT RESIDENT
        conn.commit() #END
        cur.execute("SELECT * FROM test_table") #UPDATE TABLE
        rows = cur.fetchall()
        for row in rows:
            test_table.insert('',0,text=row[0],values=row[1:])   

    #Button_Save
    save = tk.Button(root, text="Save", bg="white", command=lambda:[addresident(),addsuccesfully()])
    save.grid(row=7,column=1,pady=20)

    #Buttonn_Exit
    Exit = tk.Button(root, text="Exit", bg="white", command=add_exit)
    Exit.grid(row=7,column=2,pady=20)   

    display = tk.Label(root, text="Insert Name:", bg="white")
    display.grid(row=0,column=1,padx=60)

    name = tk.Entry(root, width=20)
    name.grid(row=0,column=2,)

    display = tk.Label(root, text="Insert Cedula:", bg="white")
    display.grid(row=1,column=1,padx=60)

    cedula = tk.Entry(root, width=20)
    cedula.grid(row=1,column=2) 

    display = tk.Label(root, text="Insert Phone:", bg="white")
    display.grid(row=2,column=1,padx=60)

    phone = tk.Entry(root, width=20)
    phone.grid(row=2,column=2)

    display = tk.Label(root, text="Insert Mod:", bg="white")
    display.grid(row=3,column=1,padx=60)

    mod = tk.Entry(root, width=20)
    mod.grid(row=3,column=2)  

    display = tk.Label(root, text="Insert Status:", bg="white")
    display.grid(row=4,column=1,padx=60)

    status = tk.Entry(root, width=20)
    status.grid(row=4,column=2)

    root.mainloop()


#PRINCIPAL WINDOW

database = 'database.db'

root1 = tk.Tk()
root1.title("PAY TO RENT")
root1.geometry("1100x600") #Geometry
root1.config(bg="white")


def exit():
    root1.destroy()

def please_select():
    display = tk.Label(root1, text="Please select a resident")
    display.grid(row=13,column=11,columnspan=3)
    display.config(bg="white", fg="red")

def resident_succesfully_deleted():
    display = tk.Label(root1, text="Resident_succesfully_deleted")
    display.grid(row=13,column=11,columnspan=3)
    display.config(bg="blue", fg="red")    

def create_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
    except Error as e:
        print(e)
    return conn

def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM test_table")
    rows = cur.fetchall()
    for row in rows:
        test_table.insert('',0,text=row[0],values=row[1:])      

def delete():
    conn = sqlite3.connect(database)
    try:
        test_table.item(test_table.selection())['text'][0] #Select a row 
    except IndexError as e:
        please_select() # Error
    return
    resident = test_table.item(test_table.selection())['text']
    cur = conn.cursor()
    cur.execute('DELETE FROM test_table WHERE CEDULA =?',resident) #THE BUG
    new = test_table.get_children()#CLEANING TABLE
    for element in new:
        test_table.delete(element)
    conn.commit() #END
    cur.execute("SELECT * FROM test_table") #UPDATE TABLE
    rows = cur.fetchall()
    for row in rows:
        test_table.insert('',0,text=row[0],values=row[1:])
    resident_succesfully_deleted()


#Table
test_table = ttk.Treeview(height=20,columns=("#0","#1","#2","#3"))
test_table.grid(row=2,column=2,rowspan=10,columnspan=20,pady=40,padx=40)
test_table.heading("#0", text="Name",anchor = CENTER)
test_table.heading("#1", text="Cedula",anchor = CENTER)
test_table.heading("#2", text="Phone",anchor = CENTER)
test_table.heading("#3", text="Contract",anchor = CENTER)
test_table.heading("#4", text="Status",anchor = CENTER)

#Button1
add = tk.Button(root1, text="Add", bg="white", command=add)
add.grid(row=12,column=11)

#Button2
delete = tk.Button(root1, text="Delete", bg="white", command=delete)
delete.grid(row=12,column=12)

#Button3
Exit = tk.Button(root1, text="Exit", bg="white", command=exit)
Exit.grid(row=12,column=13)

conn = create_connection(database)
select_all_tasks(conn)

root1.mainloop()
