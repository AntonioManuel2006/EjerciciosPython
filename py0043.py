# Solicitar la cadena al usuario
texto = input("Introduce una cadena de texto: ")

# Lista para almacenar caracteres ya contados
caracteres_contados = []

# Recorrer cada carácter
for i in range(len(texto)):
    caracter = texto[i]
    if caracter not in caracteres_contados:
        contador = 0
        # Contar ocurrencias del carácter
        for j in range(len(texto)):
            if texto[j] == caracter:
                contador += 1
        print(f"'{caracter}' aparece {contador} veces")
        caracteres_contados.append(caracter)