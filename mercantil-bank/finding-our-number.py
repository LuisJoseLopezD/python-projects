#finding-our-number

##cedula = []
##
##for i in range(8):
##    numeros = int(input("Isert your cedula: "))
##    cedula.append(numeros)
##
##print("Your numbers are the last 3 ones from your cedula ")
##print(cedula[5],cedula[6],cedula[7])

##cedula = input("Insert your cedula: ")
##list(cedula)
##
##print("Your numbers are the last 3 ones from your cedula: ")
##print(cedula[5],cedula[6],cedula[7])

i=0;
cedula = input("Insert your cedula: ")
list(cedula)

print("Your numbers are the last 3 ones from your cedula: ")
print(cedula[i-3],cedula[i-2],cedula[i-1])
