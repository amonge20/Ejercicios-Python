# En un restaurante el menú consta de las siguientes opciones:
# Ensalada mixta ———————— 12 EU
# Sopa de pescado ——————— 10 EU
# Dorada al horno ———————— 18 EU
# Arroz al curry ————————— 14 EU
# Lasaña de carne ——————— 15 EU
# Brownie de chocolate ————— 8 EU
# Helado ——————————— 6 EU
# Refrescos —————————— 5,5 EU
# Café ———————————— 3,5 EU
# Escribe un script que lea la cantidad de cada alimento consumido y que calcule e imprima el total
# de la cuenta.

# 1. Pedimos las variables del precio de cada plato
Ensalada_Mixta_Precio = 12.0
Sopa_de_Pescado_Precio = 10.0
Dorada_al_Horno_Precio = 18.0
Arroz_al_Curry_Precio = 14.0
Lasaña_de_Carne_Precio = 15.0
Brownie_de_Chocolate_Precio = 8.0
Helado_Precio = 6.0
Refrescos_Precio = 5.5
Cafe_Precio = 3.5

# 2. Escribimos la racion de cada plato que pedira el usuario
Cantidad_Ensalada_Mixta = int(input("¿Cantidad de ensalada mixta?"))
Cantidad_Sopa_de_Pescado = int(input("¿Cantidad de sopa de pescado?"))
Cantidad_Dorada_al_Horno = int(input("¿Cantidad de dorada al horno?"))
Cantidad_Arroz_al_Curry = int(input("¿Cantidad de arroz al curry?"))
Cantidad_Lasaña_de_Carne = int(input("¿Cantidad de lasaña de carne?"))
Cantidad_Brownie_de_Chocolate = int(input("¿Cantidad de brownie de chocolate?"))
Cantidad_Helado = int(input("¿Cantidad de helado?"))
Cantidad_Refrescos = int(input("¿Cantidad de refrescos?"))
Cantidad_Cafe = int(input("¿Cantidad de cafe?"))

# 3. Calculamos la cantidad de platos que ha pedido el usuario
cuenta = ((Ensalada_Mixta_Precio * Cantidad_Ensalada_Mixta) + 
          (Sopa_de_Pescado_Precio * Cantidad_Sopa_de_Pescado) + 
          (Dorada_al_Horno_Precio * Cantidad_Dorada_al_Horno) + 
          (Arroz_al_Curry_Precio * Cantidad_Arroz_al_Curry) + 
          (Lasaña_de_Carne_Precio * Cantidad_Lasaña_de_Carne) + 
          (Brownie_de_Chocolate_Precio * Cantidad_Brownie_de_Chocolate) +
          (Helado_Precio * Cantidad_Helado) +
          (Refrescos_Precio * Cantidad_Refrescos) +
          (Cafe_Precio * Cantidad_Cafe))

# 4. Y finalmente mostraremos lo que tiene que pagar el usuario
print("Lo que tiene que pagar en total es: ",cuenta)