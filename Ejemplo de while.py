     
# Ejemplo de uso de la instrucción while en Python para calcular la suma de los primeros n números naturales
# while en Python se usa para repetir un bloque de código mientras una condición sea verdadera(True).
# La sintaxis de la instrucción while es:
# while condición:
# Inicializamos una variable para el número y otra para el resultado de la suma
n = 10
suma = 0
contador = 1

# Usamos un bucle while para calcular la suma de los primeros n números naturales
while contador <= n:
    suma += contador
    contador += 1

print(f"La suma de los primeros {n} números naturales es: {suma}")