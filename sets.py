"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
print("\033c")

set1={"python","SQL","estructurado"}
print(set1)

for i in set1:
    print(i)

set2={"hola",True,33,3.1416}
print(set2)
set2_respaldo=set2.copy()
set2.clear()
print(set2_respaldo)
set3={""}
print(set3)

set3.add("hola")
set3.add(3)
set3.add(10.0)
print(set3)

set3.pop()
set3.pop()
print(set3)

lista=[10,9,5,8,5,8,3,4,2,1]
conjuto=set(lista)
lista=list(conjuto)
print(lista)

#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

# #Solucion 1
emails = []

resp = True
while resp:
    nuevo_email = input("Email: ").strip().lower()
    
    # 1. Validar que sea de la UTD (opcional, pero ideal para el ejercicio)
    if not nuevo_email.endswith("@utd.edu.mx"): # O el dominio que usen en tu escuela
        print("Error: El correo debe pertenecer a la UTD.")
        continue # Regresa al inicio del ciclo sin guardar nada
        
    # 2. Validar que no esté duplicado
    if nuevo_email not in emails:
        emails.insert(0, nuevo_email)
        print("Email registrado con éxito.")
    else:
        print("Este email ya ha sido registrado anteriormente.")
        
    # Preguntar si desea continuar
    opcion = input("¿Deseas capturar otro email (Si/No)? ").strip().lower()
    if opcion == "no" or opcion == "n":
        resp = False

print("\nLista final de alumnos (Solución 1):")
print(emails)


# #Solucion 2
emails=[]

resp=True
while resp:
    emails.insert(0,input("Email: ").strip())
    resp=input("¿Deseas capturar otro email (Si/No)? ").upper().strip()
    if resp=="NO":
        resp=False

emails_set=set(emails)
emails=list(emails_set)
print(emails)