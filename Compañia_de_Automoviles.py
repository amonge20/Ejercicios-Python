# Una compañía de automóviles vende tres tipos de coche: RBM Serie 1, RMB Serie plus, RBM
# todoterreno. Cada uno de estos coches tiene un precio de venta y el vendedor recibe una
# comisión diferente por cada tipo de coche que ha vendido.
# Suponga que los precios y las comisiones son:
# RBM Serie 1:
# precio: 20.000 EU, comisión: 3%
# RMB Serie plus:
# precio: 35.000 EU, comisión: 5%
# RBM todoterreno:
# precio: 60.000 EU, comisión: 7%
# Crea un programa donde el usuario introduzca el numero de coches vendidos de cada tipo ese
# mes y que le devuelva la cantidad en euros a comisionar ese mes.

# Declaracion de las variables
precio_RBM_Serie_1 = int(20000)
precio_RBM_Serie_Plus = int(35000)
precio_RBM_todoterreno = int(60000)
comision_RBM_Serie_1 = float(3.0)
comision_RBM_Serie_Plus = float(5.0)
comision_RBM_todoterreno = float(7.0)
coste_total_RBM_Serie_1 = float(0.0)
coste_total_RBM_Serie_Plus = float(0.0)
coste_total_RBM_todoterreno = float(0.0)

# Preguntamos al vendedor sobre cuantos coches de cada uno de los 3 modelos RBM se han vendido y el coste total de las comisiones
RBM_Serie_1_vendidos = int(input("De la marca de coche de RBM Serie 1, ¿Cuantos coches se han vendido?"))
RBM_Serie_Plus_vendidos = int(input("De la marca de coche de RBM Serie Plus, ¿Cuantos coches se han vendido?"))
RBM_Serie_Todoterreno_vendidos = int(input("De la marca de coche de RBM Serie todoterreno, ¿Cuantos coches se han vendido?"))

# Calculamos entre el precio del coche más los coches que se vendieron junto con la comision de cada coche
coste_total_RBM_Serie_1 = RBM_Serie_1_vendidos * precio_RBM_Serie_1 * (comision_RBM_Serie_1 / 100)
coste_total_RBM_Serie_Plus = RBM_Serie_1_vendidos * precio_RBM_Serie_1 * (comision_RBM_Serie_Plus / 100)
coste_total_RBM_todoterreno = RBM_Serie_1_vendidos * precio_RBM_Serie_1 * (comision_RBM_todoterreno / 100)

# Suma total de la comision del mes
comision_Total_mes = coste_total_RBM_Serie_1 + coste_total_RBM_Serie_Plus + coste_total_RBM_todoterreno

# Resultado de cada coche
print("\n Comisión mensual por modelo:")
print(f" RBM Serie 1: {coste_total_RBM_Serie_1:.2f} €")
print(f" RBM Serie Plus: {coste_total_RBM_Serie_Plus:.2f} €")
print(f" RBM Todoterreno: {coste_total_RBM_todoterreno:.2f} €")