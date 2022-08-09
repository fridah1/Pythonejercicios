#Ingresas un número y te indicia si es primo, y cuantos contadores y divisores tiene.
n=int(input("Ingrese un numero ")) 

contador=1
divisores=0

while contador<=n:
  residuo=n%contador
  print(residuo)
  if residuo == 0:
    divisores=divisores+1
  contador=contador+1

if divisores==2:
  print ("es primo")
  print("Tiene ",divisores, " divisores")
else:
  print("no es primo")
  print("Tiene ",divisores, " divisores")
