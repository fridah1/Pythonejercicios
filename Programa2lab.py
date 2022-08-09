#Ingresas un texto, luego le quita los espacios, y te indica si es palíndromo o no.

a = str(input("Ingrese un texto: "))
#Se quitan los espacios del texto
b = a.replace(" ","")
#Se junta y se pone al revés la palabra
c = "".join(reversed(b))
print(c)
#Aquí dice si las frase son iguales
if b == c:
 print("Si es un palindromo :)")
else:
 print("No es un palindromo :(")
