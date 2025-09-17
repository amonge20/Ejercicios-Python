# a. Crea un script en el que el usuario introduzca un número de más de una cifra. El script debe
# imprimir los componentes del número uno a uno por pantalla. Por ejemplo si el número introducido
# es el 4532 por pantalla deberá imprimirse:
# 4
# 5
# 3
# 2
# b. Crea un script que dado un numero entero de cuatro cifras calcula e imprima el número que
# resulta de leer el número introducido de derecha a izquierda. Por ejemplo si el número introducido
# es 4532, el output deberá ser 2354.

# Array para guardar los numeros
lista_de_numeros = []

# Preguntamos al usuario sobre que numeros quiere introducir
print("Introduce una cantidad de numeros: ")
lista_de_numeros = input()

# Reordenamos esos numeros verticalmente
numeros_verticales = "\n".join(lista_de_numeros)
print("Ejercicio A: Numeros ordenados verticalmente")
print(numeros_verticales)

# Reordenamos a la inversa los numeros introducidos
print("Ejercicio B: Numeros introducidos al reves")
numeros_reversa = int(str(lista_de_numeros)[::-1])
print(numeros_reversa)