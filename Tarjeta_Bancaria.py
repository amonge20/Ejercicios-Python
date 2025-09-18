# Crea un script que reciba como input un número de tarjeta de crédito e imprima por pantalla todos
# los caracteres en forma de asterisco salvo los últimos cuatro. Si por ejemplo el número de tarjeta
# es 1234 2345 3456 5678, el output deberá ser **** **** **** 5678.

# Introducimos la tarjeta de credito (Nos lo inventamos)
Numero_Tarjeta = int(input("Introduce tu tarjeta de credito (maximo 16 digitos): "))

# Convertimos el int de la variable 'Numero_Tarjeta' en cadena
Cadena_Tarjeta = str(Numero_Tarjeta)

# Remplazamos los numeros por '****' y mostraremos el resultado con la cadena substituida pero solo mostrando los ultimos 4 digitos
Numeros_Ocultos = Cadena_Tarjeta.replace(Cadena_Tarjeta, " **** **** **** ")
print(Numeros_Ocultos, Cadena_Tarjeta[12:17])