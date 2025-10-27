try:
    numero = int(input("Introduce un número entero: "))
    while numero % 2 != 0:
        print("El número es impar. Intenta de nuevo.")
        numero = int(input("Introduce un número entero: "))

except ValueError:
    print("Eso no es un número entero válido.")