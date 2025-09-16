# Una casa de cambios necesita construir un programa que dada una cantidad de euros introducida
# por el usuario de el resultante en dólares.
# 1. Crea un script que reciba una cantidad de euros del usuario e imprima por pantalla el
# correspondiente en dólares (considera una tasa de cambio donde 1 EU = 1.2 $)
# 2. La casa de cambios se queda un 10% en concepto de ‘tasas de gestión’. Calcula el monto
# recibido, el cambio en dólares, la cantidad que se queda la casa de cambios y la cantidad de
# dólares restante que recibirá el usuario. Imprime el desglose por pantalla formateado de tal
# forma que quede claro para el usuario. 

# Numero del dolar
USD = 1.20
# tasa de gestion
tasa_de_gestion = 10

# Preguntamos la cantidad de dinero al usuario
convertidor_moneda = float(input("Introduce la cantidad de 'EUR' y luego despues se mostrara la cantidad de 'EUR' en 'USD': "))
# La casa de cambios se queda un 10% en concepto de 'tasas de gestion'
resutado_con_tasa_de_gestion = convertidor_moneda * (USD / tasa_de_gestion)
resutado_con_tasa_de_gestion = round(resutado_con_tasa_de_gestion,2)
resutado_con_usuario = convertidor_moneda - resutado_con_tasa_de_gestion
resutado_con_usuario = round(resutado_con_usuario,2)
print("Tasa de gestion: ",resutado_con_tasa_de_gestion)
print("El monto que recibe el usuario: ",resutado_con_usuario)