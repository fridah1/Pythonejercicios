#Aquí pedimo una palabra 
x=str(input("Ingrese una palabra:"))
#Aquí vamos a buscar la inicial de la palabra
j= x[0]
#Aquí dice que si la primera letra de la palabra, es una vocal ya sea mayúscula o minúscula le va a poner "Inicia con vocales"
if j =="a" or j == "e" or j == "i" or j == "o" or j == "u" or j == "A" or j == "E" or j =="I" or j == "O" or j == "U": 
  print("Inicia con vocales")
  #Aquí dice que si la primera letra de la palabra no está en esa lista, va a ser consonante
else:
   print("Inicia con consonantes")

  
