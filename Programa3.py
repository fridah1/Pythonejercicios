#Ingresas dos numeros e indica cual de los dos es menor, y si pones los mismos te indica que son iguales. 
n1=int(input("Ingrese numero 1:"))
n2=int(input("Ingrese numero 2:"))

if n1<n2:
  print("El primer numero es menor")
if n2<n1:
  print("El segundo numero es menor")
if n1==n2:
    print ("Ambos numeros son iguales")
