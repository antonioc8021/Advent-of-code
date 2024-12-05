# Ruta del archivo cargado
file_path = "C:/Users/anton/Desktop/WorkSpace/Advent of code/day2/input_day2.txt"

# Crear el diccionario
line_dict = {}

# Leer el archivo y construir el diccionario
with open(file_path, "r") as file:
    for line_number, line in enumerate(file):
        # Convertir cada línea en una lista de números
        numbers = [int(num) for num in line.split() if num.isdigit()]
        # Agregar la lista al diccionario con el número de línea como clave
        line_dict[line_number] = numbers

# Imprimir el diccionario
print(line_dict)
