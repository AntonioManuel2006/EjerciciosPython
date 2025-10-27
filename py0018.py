
registro = "zeréP nauJ,01"
# Invertir la cadena
registro_corregido = registro[::-1]  # Resultado: "10,Juan Pérez"
# Separar nota y nombre
nota, nombre = registro_corregido.split(',')
# Mostrar el mensaje
print(f"{nombre} ha sacado una nota de {nota}.")


