#Ingresas el producto que llevarás, el precio, y la cantidad, y luego te indica el precio sin descuento, con descuento, y cuanto te ahorras. 
n1=str(input("ingrese producto"))
print (n1)
n2=float(input("ingrese precio de producto"))
print (n2)
n3=float(input("ingrese cantidad de producto"))
print (n3)

if n3 >= 5: 
  res1=n2*n3
  print ("precio sin descuento")
  print (res1)

  res3=n2*n3*0.35

  res2= res1-res3
  
  print ("precio con descuento")
  print (res2)
   
  print ("ahorro")
  print (res3)

else: 
  res1=n2*n3
  print ("precio sin descuento")
  print (res1)
