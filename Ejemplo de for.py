# Ejemplo de uso de la instrucción for en Python
#la instruccion for se utiliza para crear bucles que se repiten un número determinado de veces
#o para iterar sobre una secuencia de elementos, como una lista o un diccionario.

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Usando un bucle for con comprensión de listas para crear una nueva lista con los cuadrados de los números
cuadrados = [numero ** 2 for numero in numeros]
print(f"Los cuadrados de los números son: {cuadrados}")

# Definiendo una función que devuelve el cubo de un número
def cubo(n):
    return n ** 3

# Usando un bucle for para aplicar la función cubo a cada número en un rango y almacenarlo en una lista
cubos = [cubo(i) for i in range(6, 11)]
print(f"Los cubos de los números del rango son: {cubos}")

# Usando un bucle for para iterar sobre un diccionario y mostrar sus elementos
diccionario = {'a': 1, 'b': 2, 'c': 3}
for clave, valor in diccionario.items():
    print(f"La clave es: {clave} y el valor es: {valor}")