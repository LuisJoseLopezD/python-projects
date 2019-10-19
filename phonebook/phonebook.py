# AGENDA TELEFONICA SIMPLE.

# FUNCIONES

import sys

def agregarcontacto():
    archivo = open("Agenda.csv","a")
    nombre = input("Nombre del contacto: ")
    telefono = input("Numero de telefono: ")
    print("Contacto agregado: ",nombre,telefono)
    archivo.write(nombre)
    archivo.write(" ")
    archivo.write(telefono)
    archivo.write("\n")
    archivo.close()
    opciones()

def mostrarlista():
    print("Lista de contactos: ")
    archivo = open("Agenda.csv")
    print(archivo.read())
    archivo.close()
    opciones()
  
def salir():
    print("Agenda telefonica simple.")
    print("Realizado por Luis Jose Lopez Delgado")
    sys.exit()

def opciones():
    print("¿Desea realizar otra operación?")
    print("Escriba 'si' o 'no'")
    respuesta = input("")

    if respuesta == "si":
         agenda()

    if respuesta == "no":    
        salir()    

        
# COMIENZA EL MENU

def agenda():
    print("Agenda telefonica simple.")
    print()
    print("1. Agregar contacto.")
    print("2. Mostrar lista de contactos.")
    print("3. Salir.")

    opcion = int(input(""))

    if opcion == 1:
        agregarcontacto()

    elif opcion == 2:
        mostrarlista()

    elif opcion == 3:
        salir()

agenda()        
    
