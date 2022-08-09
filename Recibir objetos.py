#Ingresas objetos y te los va poniendo en lista, y cuando quiera sterminarla pones "fin" y ya no sigue.
o=str(input("ingrese un objeto: "))
clave="fin" 
lista = []
while clave != o:
 o=str(input("ingrese un objeto: "))
lista.append(o)
print(lista)
