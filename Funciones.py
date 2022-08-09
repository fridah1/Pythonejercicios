#Ingresas el largo y ancho de un terrento, luego los multiplica, te da el resultado, y luego te pregunta si quieres continuar, si pones "si" el programa continúa,
si pones "no", el porgrama para. 
alto=int(input("Ingrese el largo del terreno:")) 
ancho=int(input("Ingrese el ancho del terreno:"))
def multiplicacion(alto,ancho): 
  resultado=alto*ancho
  print(resultado) 
multiplicacion(alto,ancho)

c=str(input("¿Quiere continuar?")) 
cl= "si"
cla="no"

if c==cla:
  print("Usted ha finalizado")

while c!=cla: 
 alto=int(input("Ingrese el largo del terreno:")) 
 ancho=int(input("Ingrese el ancho del terreno:"))
 def multiplicacion(alto,ancho): 
  resultado=alto*ancho
  print(resultado) 
 multiplicacion(alto,ancho)

c=str(input("¿Quiere continuar?"))
cl= "si"
cla="no"
if c==cla:
  print("Usted ha finalizado")
