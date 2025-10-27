# python
print("CALCULADORA\nSumar  Restar  Multiplicar  Dividir")

opcion = ""
while opcion != "salir":
    opcion = input("Elige operación (o 'salir'): ").lower()
    if opcion == "salir":
        print("Saliendo...")
        break

    if opcion == "sumar" or opcion == "restar" or opcion == "multiplicar" or opcion == "dividir":
        a = input("Primer número (o 'salir'): ")
        if a.lower() == "salir":
            print("Saliendo...")
            break
        b = input("Segundo número (o 'salir'): ")
        if b.lower() == "salir":
            print("Saliendo...")
            break

        try:
            n1, n2 = float(a), float(b)
        except ValueError:
            print("Número inválido.")
            continue

        if opcion == "sumar":
            res = n1 + n2
        elif opcion == "restar":
            res = n1 - n2
        elif opcion == "multiplicar":
            res = n1 * n2
        else:  # dividir
            if n2 == 0:
                print("Error: división por cero.")
                continue
            res = n1 / n2

        print(f"Resultado: {res}")
    else:
        print("Operación no válida.")

