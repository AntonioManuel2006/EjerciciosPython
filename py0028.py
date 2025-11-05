print("Pizzería La Beata")
saldo = float(input("Introduce el dinero que tienes disponible: "))
print(f"Tu saldo es de: {saldo:.2f}$")
# Precios de las pizzas
precio_margarita = 8.95
precio_pepperoni = 9.95
precio_hawaiana = 10.50
# Precios de los ingredientes extra
precio_extra_queso = 1.25
precio_champiñones = 1.50
precio_jamon = 1.75
# Mostrar menú de pizzas
print("Pizzas disponibles:")
print(f"1. Margarita - {precio_margarita:.2f}$")
print(f"2. Pepperoni - {precio_pepperoni:.2f}$")
print(f"3. Hawaiana - {precio_hawaiana:.2f}$")
# Selección de pizza
eleccion_pizza = int(input("Elige el número de la pizza que deseas: "))
if eleccion_pizza == 1:
    precio_pizza = precio_margarita
    nombre_pizza = "Margarita"
elif eleccion_pizza == 2:
    precio_pizza = precio_pepperoni
    nombre_pizza = "Pepperoni"
elif eleccion_pizza == 3:
    precio_pizza = precio_hawaiana
    nombre_pizza = "Hawaiana"
else:
    print("Opción no válida. Vuelve a empezar.")
    exit()
saldo -= precio_pizza
print(f"Has elegido {nombre_pizza}. Precio: {precio_pizza:.2f}$. Saldo restante: {saldo:.2f}$")
# Ingredientes extra
ingredientes_extra = {
    1: ("Extra de queso", precio_extra_queso),
    2: ("Champiñones", precio_champiñones),
    3: ("Jamón", precio_jamon)
}
total_ingredientes = 0.0
while True:
    añadir_extra = input("¿Quieres añadir ingredientes extra? (s/n): ").strip().lower()
    if añadir_extra == 's':
        print("Ingredientes extra disponibles:")
        for key, (nombre, precio) in ingredientes_extra.items():
            print(f"{key}. {nombre} - {precio:.2f}$")
        eleccion_extra = int(input("Elige el número del ingrediente extra que deseas (0 para terminar): "))
        if eleccion_extra == 0:
            break
        elif eleccion_extra in ingredientes_extra:
            nombre_extra, precio_extra = ingredientes_extra[eleccion_extra]
            total_ingredientes += precio_extra
            saldo -= precio_extra
            print(f"Has añadido {nombre_extra}. Precio: {precio_extra:.2f}$. Saldo restante: {saldo:.2f}$")
        else:
            print("Opción no válida.")
    elif añadir_extra == 'n':
        break
    else:
        print("Opción no válida.")
# Comprobar saldo y mostrar ticket
total_pedido = precio_pizza + total_ingredientes
if saldo >= 0:
    print("\n--- Su Pedido ---")
    print(f"Pizza: {nombre_pizza} - {precio_pizza:.2f}$")
    if total_ingredientes > 0:
        print(f"Ingredientes extra: {total_ingredientes:.2f}$")
    print(f"Total de su pedido: {total_pedido:.2f}$")
    print(f"Su cambio de {saldo + total_pedido:.2f}$ es: {saldo:.2f}$")
else:
    print("No tienes suficiente dinero para completar el pedido. Vuelve a empezar.")

