# Numero del dolar
USD = 1.20

# Preguntamos la cantidad de dinero al usuario
convertidor_moneda = float(input("Introduce la cantidad de 'EUR' y luego despues se mostrara la cantidad de 'EUR' en 'USD': "))
# Calcula el resultado dela cantidad de EUR pedido + rondedeamos el resultado 
resutado = convertidor_moneda * USD
resutado = round(resutado,2)
print(convertidor_moneda,"€, en dolares se convierte en $",resutado)