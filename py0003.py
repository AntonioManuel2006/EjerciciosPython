
#Parte A
asistentes = []
while True:
    nombre = input("Escribe el nombre del asistente a añadir (fin para salir): ")
    if nombre.strip().lower()=="fin":
        break
    asistentes.append(nombre)
print(f"Asistentes: {asistentes}")
#Parte B
nombre2 = input("Escribe el nombre del que quieres ver el numero de repeticiones: ")
print(f"El nombre aparece {asistentes.count(nombre2)} veces")

#Parte C
indice = asistentes.index(nombre2)
print(f"El nombre aparece por primera vez en la posicion {indice}")
asistentes.pop(indice)

#Parte D
nombre3 = input("Escribe el nombre del asistente VIP: ")
asistentes.insert(0, nombre3)
print("Lista de asistentes actualizada:")
print(asistentes)