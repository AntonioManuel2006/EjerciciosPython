texto = input("Introduce una cadena de texto: ")
caracter_reemplazado = input("Introduce el carácter a reemplazar: ")
caracter_nuevo = input("Introduce el nuevo carácter: ")

if len(caracter_reemplazado) > 1 or len(caracter_nuevo) > 1:
    print("Error: Debes introducir un solo carácter para reemplazar y uno nuevo.")
else:
    texto_modificado = ""
    for caracter in texto:
        if caracter == caracter_reemplazado:
            texto_modificado += caracter_nuevo
        else:
            texto_modificado += caracter
    print("Cadena modificada:", texto_modificado)

