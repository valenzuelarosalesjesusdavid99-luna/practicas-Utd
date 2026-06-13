"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables
 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""

print("\033c")
#Funciones más comunes en las listas
paises=["mexico","canada","EUA","brasil"]

numero=[123,45,8,24]


varios=["HOLA",3,1416,33,True]

vacia=[]
#Imprimir el contenido de una lista
print(paises)
print(numero)
print(varios)
print(vacia)

print(paises[1])


#Recorrer la lista 
#1er forma 
paises.pop(1)
print(paises)

# #2do forma 
paises.remove("brasil")
print(paises)


#ordenar elementos de una lista
paises=["mexico","canada","EUA","brasil"]
print(paises)
paises.sort()
print(paises)

#dar la vuelta a una lista
paises.reverse
print(paises)


#Agregar, insertar, Añadir un elemento a una lista
#1er forma 
paises.append("Ecuador")
print(paises)

#2da forma
paises.insert(1,"argentina")
print(paises)
paises.insert(8,"españa")
print(paises)
#Eliminar, borrar, suprimir, un elemento de una lista
#1er forma


#2da forma 


#Buscar un elemento dentro de la lista
resp="brasil" in paises
print(resp)

#Contar el numeros de veces que aparece un elemento dentro de una lista
numero=(12,34,56,7,100,200,0,-1,-10,23,24,8,23,50)
print(numero)
num=int(input("Dame un numero: "))
cuantos=numero.count(num)
print(f"el numero de veces que aparace el {num} es: {cuantos} ")

#Conocer la posicion o indice en el que se encuentra un elemento de la lista
posicion=numero.index(100)
print(f"la posicion de numeros es: {posicion}")

#Unir el contenido de una lista dentro de otra lista
numero=(12,34,56,7,100,200,0,-1,-10,23,24,8,23,50)
print(numero)
numero2=[500,1000]
print(numero2)
numero.extend(numero)
print(numero)
#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente

numero.sort()


