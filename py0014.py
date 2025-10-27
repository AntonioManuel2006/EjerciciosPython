
try:
    num1 = float(input("Introduce el primer número (15%): "))
    num2 = float(input("Introduce el segundo número (35%): "))
    num3 = float(input("Introduce el tercer número (50%): "))

    media_ponderada = (num1 * 0.15) + (num2 * 0.35) + (num3 * 0.50)
    print("La media ponderada es: {:.2f}".format(media_ponderada))
except ValueError:
    print("Error: Debes introducir un número válido.")