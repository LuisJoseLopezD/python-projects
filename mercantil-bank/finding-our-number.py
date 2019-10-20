#finding-our-number

##cedula = []
##
##for i in range(8):
##    numeros = int(input("Ingrese su cedula: "))
##    cedula.append(numeros)
##
##print("Su numero son los 3 ultimos digitos de su cedula: ")
##print(cedula[5],cedula[6],cedula[7])

##cedula = input("Ingrese su cedula: ")
##list(cedula)
##
##print("Su numero son los 3 ultimos digitos de su cedula: ")
##print(cedula[5],cedula[6],cedula[7])

i=0;
cedula = input("Ingrese su cedula: ")
list(cedula)

print("Su numero son los 3 ultimos digitos de su cedula: ")
print(cedula[i-3],cedula[i-2],cedula[i-1])
