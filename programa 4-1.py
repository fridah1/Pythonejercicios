#Ingresas un texto, luego la letra que quieras, y cuenta cuantas veces se repite esa letra. 
x= str(input("Ingrese el texto:"))
y= str(input("Ingrese una letra:"))

contador = 0
for l in x:
  if l == y:
    contador += 1
print ("Se repitieron",contador,"veces letra", y)
