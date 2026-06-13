import os

print("\033c")
#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numero=[10,34,25,45]

print(numero)

lista="["
for i in numero:
    lista+=f"{i} ,"
print(f"{lista}]")
    
while(lista):
 lista="["
for i in range(0,len(numero)):
    lista+=f"{numero[i]} ,"
print(f"{lista}]")
    

#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
palabras=["UTD","segundo","TI","MTI"]
palabras=input("dame una palabra a buscar").strip()

if palabras in palabras:
   print("encontre la palabra en la lista")
else:
   print("no encontre la palabra la lista")

#2DA FORMA
palabras=["UTD","segundo","TI","MTI"]
print(palabras)
palabras=input("dame una palabra a buscar").strip()
encotro=False
for i in palabras:
   if i==palabras:
      encotro=True
if encotro:
   print("encontre la palabra en lista")
else:
   print("no encontre la palabras en lista")

#3er FORMA
palabras=["UTD","segundo","TI","MTI"]
print(palabras)
palabras=input("dame una palabra a buscar").strip()
encotro=False
for i in range(0,len(palabras)):
   if palabras[i]==palabras:
      encotro=True
if encotro:
   print("encontre la palabra en lista")
else:
   print("no encontre la palabras en lista")

#Ejemplo 3 Añadir elementos a la lista

lista=[]

true=True

while true:
  dato=input("dame un valor para  lista").upper().strip()
  lista.append(dato)
  true=input("deseas añadir mas elementos a lista (si\no)").lower().strip()
  if true=="no":
     true=False

true="si"
while true=="si":
  dato=input("dame un valor para  lista").upper().strip()
  lista.append(dato)
  true=input("deseas añadir mas elementos a lista (si\no)").lower().strip()
  


print(lista)


#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda
agenda=[
       ["carlos","61812367"]
       ["alberto","61824423"]
       ["martin", "61822092"]
]   


print(agenda)

for i in agenda:
   print(i)

for c in range(0,2):
   for r in range(0,3):
      print(agenda[c] [r])

lista=""
for r in range(0,3):
   for c in range(0,2):
      lista+=f"{agenda[r][c],}"
   lista+="\n"

print("["+lista+"]")