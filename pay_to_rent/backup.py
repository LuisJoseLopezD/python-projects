from tkinter import ttk
from tkinter import *
import tkinter as tk
import sqlite3
from sqlite3 import Error

#SECONDARY WINDOW

def add():
    root = tk.Tk()
    root.title("Add Resident")
    root.geometry("500x200") #Geometria
    #tasks = [] #Lista vacia para llenarla

    def add_exit():
        root.destroy()

    display = tk.Label(root, text="Insert Name:", bg="white")
    display.grid(row=0,column=1,padx=60)

    txt_input = tk.Entry(root, width=20)
    txt_input.grid(row=0,column=2,)

    display = tk.Label(root, text="Insert Cedula:", bg="white")
    display.grid(row=1,column=1,padx=60)

    txt_input = tk.Entry(root, width=20)
    txt_input.grid(row=1,column=2) 

    display = tk.Label(root, text="Insert Phone:", bg="white")
    display.grid(row=2,column=1,padx=60)

    txt_input = tk.Entry(root, width=20)
    txt_input.grid(row=2,column=2)

    display = tk.Label(root, text="Insert Mod:", bg="white")
    display.grid(row=3,column=1,padx=60)

    txt_input = tk.Entry(root, width=20)
    txt_input.grid(row=3,column=2)  

    display = tk.Label(root, text="Insert Status:", bg="white")
    display.grid(row=4,column=1,padx=60)

    txt_input = tk.Entry(root, width=20)
    txt_input.grid(row=4,column=2)

    #Button_Save
    add_task = tk.Button(root, text="Save", bg="white", command=add)
    add_task.grid(row=5,column=1,pady=20)

    #Buttonn_Exit
    Exit = tk.Button(root, text="Exit", bg="white", command=add_exit)
    Exit.grid(row=5,column=2,pady=20)


#PRINCIPAL WINDOW

root1 = tk.Tk()
root1.title("PAY TO RENT")
root1.geometry("1100x600") #Geometria

database = 'database.db'

def delete():
    pass

def exit():
    pass

#Table
table = ttk.Treeview(height=20,columns=("#0","#1","#2","#3"))
table.grid(row=2,column=2,rowspan=10,columnspan=20,pady=40,padx=40)
table.heading("#0", text="Name",anchor = CENTER)
table.heading("#1", text="Cedula",anchor = CENTER)
table.heading("#2", text="Phone",anchor = CENTER)
table.heading("#3", text="Contract",anchor = CENTER)
table.heading("#4", text="Status",anchor = CENTER)

#Button1
add = tk.Button(root1, text="Add", bg="white", command=add)
add.grid(row=12,column=11)

#Button2
delete = tk.Button(root1, text="Delete", bg="white", command=delete)
delete.grid(row=12,column=12)

#Button3
Exit = tk.Button(root1, text="Exit", bg="white", command=exit)
Exit.grid(row=12,column=13)

root1.mainloop()