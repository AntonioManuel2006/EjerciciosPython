
usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}
administradores = {"Juan", "Marta"}
administradores.discard("Juan")
administradores.add("Marcos")
for usuarios in usuarios:
    if usuarios in administradores:
        print(f"{usuarios} es administrador")
    else:
        print(f"{usuarios} no es administraddor")

