# Gestión de inscritos en un curso utilizando conjuntos
usuarios = {"Ana", "Luis", "Carla", "Pedro"}
# Dar de alta a nuevos inscritos
while True:
    nuevo_inscrito = input("Introduce el nombre del nuevo inscrito (o 'fin' para terminar): ").strip()
    if nuevo_inscrito.lower() == "fin":
        break
        if nuevo_inscrito:
            usuarios.add(nuevo_inscrito)
        else:
            print("No has introducido un nombre válido.")
    else:
        if nuevo_inscrito:
            usuarios.add(nuevo_inscrito)
        else:
            print("No has introducido un nombre válido.")
# Dar de alta usuarios por lotes
lotes_inscritos = input("Introduce varios nombres de usuarios separados por comas: ")
nuevos_inscritos = {nombre.strip() for nombre in lotes_inscritos.split(",") if nombre.strip()}
usuarios.update(nuevos_inscritos)
# Crear una copia del conjunto
usuarios_copia = usuarios.copy()
# Dar de baja a un inscrito
nombre_baja = input("Introduce el nombre del inscrito a dar de baja: ").strip()
try:
    usuarios.remove(nombre_baja)
    print(f"{nombre_baja} ha sido dado de baja.")
except KeyError:
    print(f"{nombre_baja} no está inscrito")

# Consultar si una persona está inscrita
nombre_consulta = input("Introduce el nombre de la persona a consultar: ").strip()
if nombre_consulta in usuarios:
    print(f"{nombre_consulta} está inscrito.")
else:
    print(f"{nombre_consulta} no está inscrito.")
# Consultar si alguien de un grupo está inscrito
grupo_consulta = input("Introduce varios nombres de personas separados por comas para consultar si están inscritos: ")
nombres_grupo = {nombres.strip() for nombres in grupo_consulta.split(",") if nombres.strip()}
inscritos_en_grupo = nombres_grupo & usuarios
if inscritos_en_grupo:
    print(f"Las siguientes personas del grupo están inscritas: {', '.join(inscritos_en_grupo)}")
else:
    print("Ninguna persona del grupo está inscrita.")
# Mostrar número total de inscritos y lista ordenada
print("Numero total de inscritos:", len(usuarios))
print("Lista ordenada de inscritos:", sorted(usuarios))

