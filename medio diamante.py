#Es un patron de la mitad de un diamante.
print("Patron")
for x in range (0,10):
  for y in range (0,x+1): 
    print ("*", end="") 
  print()
for y in range (0,10):
  for x in range (0,x): 
    print ("*", end="") 
  print()
