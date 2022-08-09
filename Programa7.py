#Ingresas una letra y te indica si es vocal o no, y si es vocal te dice que si se puede procesar el dato.
n1=str(input("Ingrese una letra: "))

if n1=="a": 
    print("Es una vocal")

elif n1=="e": 
  print ("Es una vocal")

elif n1=="i": 
  print("Es una vocal")

elif n1=="o": 
  print("Es una vocal")

elif n1=="u": 
  print("Es una vocal")
 
else:
  print("No es una vocal")

if len(n1)>1: 
  print("No se puede procesar el dato")

else:
  print("Si se puede procesar el dato")
