username = "admin"
key = "1234"

def database():
    pass

def loginsystem():
    user1 = user.get()
    password1 = password.get()
    if user1 == username and password1 == key:
        print("Funcionando")
    else:
        print("mensaje de error")

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Login System")
root.geometry("400x500") #Geometry
root.config(bg='white')

image = tk.PhotoImage(file="user.png")
label = tk.Label(image=image)
label.grid(row=3,column=4,columnspan=3, padx=30)
label.config(bg='white')

display = tk.Label(root, text="USUARIO", bg="white")
display.grid(row=4,column=4,pady=20, padx=30)
display.config(bg='white')

user = tk.Entry(root, width=20)
user.grid(row=4,column=5, pady=20, padx=30)

display = tk.Label(root, text="CONTRASEÑA", bg="white")
display.grid(row=5,column=4, padx=30)

password = tk.Entry(root, width=20)
password.grid(row=5,column=5, padx=30) 

#Boton 2
delete = tk.Button(root, text="Login", bg="white", command=loginsystem)
delete.grid(row=7,column=5, pady=30, padx=70)

root.mainloop()    
