#Aquí pedimos que ingrese el primer y segundo nombre, y apellido. Luego le quita los espacios, y muestra las primeras dos letras de los nombres, y luego se unen al correo.
n= str(input("Ingrese su nombre: "))
a = str(input("Ingrese su segundo nombre: "))
a2 = str(input("Ingrese sus apellidos: "))
#Aquí quitamos los espacios para que el correo quede junto
a3 = a2.replace(" ","")

#Esto muestra las primeras dos letras de los nombres 
a = n[0]+n[1]
#Aquí los nombres y appelidos se unen en el correo
print(a+"."+a3+"@baco.com")
