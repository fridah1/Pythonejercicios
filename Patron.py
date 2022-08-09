#Realiza un patron de estrellas y que formen la mitad de un triángulo.
print("Patron")
for x in range (0,10):
  for y in range (0,x+1): #es el que hace que sea vertical 
    print ("*", end="") #ese end es un espacio, ahi termina la linea pero deja un espacio 
  print()

