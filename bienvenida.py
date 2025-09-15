# Preguntamos por el nombre del usuario
print("¿Como te llamas? ")
nombre = input()
print("¿Pero como te llamas realmente? ")
nombre_punto = input()
# Variables para mostrar el resultado del print
bienvenido = "Hola"
variable_bienvenido = ", estas usando python!"

# Mostramos el resultado "hola Aitor, estas usando python!"
# Frase normal
print("Frase normal: ", bienvenido, nombre.title(), variable_bienvenido)
# Si queremos que la frase sea en mayuscula
print("Frase en mayuscula: ", bienvenido.upper(), nombre.upper(), variable_bienvenido.upper())
# Si queremos que la frase sea en minuscula
print("Frase en minuscula: ", bienvenido.lower(), nombre.lower(), variable_bienvenido.lower())
# Si queremos que el formato del nombre sea el correcto
print("Frase del nombre correcto: ", bienvenido, nombre.title(), variable_bienvenido)
# Si queremos eliminar que en el nombre tiene un punto o una coma
print("Frase del nombre correcto 2: ", bienvenido, nombre_punto.replace(".",""), variable_bienvenido)
print("Frase final: ", bienvenido, nombre.title(), variable_bienvenido)