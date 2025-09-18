# a. Crea un script que muestre por pantalla el resultado de la siguiente operación aritmética:

            # (3+2)ª
            # -----
            # (2x5)

# b. Escribe un programa que lea un entero positivo, n, introducido por el usuario y después
# muestre por pantalla el resultado de la siguiente operación:

            # n(n+1)
            # ------
            #   2
            
# c. Escribe un programa que pida al usuario dos números enteros y muestre por pantalla los
# números de entrada, el cociente y el resto. 

# Punto A
Numero_1 = int(input("Introduce el primer numero de la operacion A: "))
Numero_2 = int(input("Introduce el segundo numero de la operacion A: "))
Numero_3 = int(input("Introduce el tercer numero de la operacion A: "))
Numero_4 = int(input("Introduce el cuarto numero de la operacion A: "))

# Operacion del Punto A
Operacion_A = (Numero_1 + Numero_2 / Numero_3 * Numero_4) ** 2

# Punto B
Numero_n = int(input("Introduce un numero que sera 'n' en la operacion B: "))

# Operacion del punto B
Operacion_B = Numero_n * (Numero_n + 1) / 2

# Punto C
Numero_Entero_1 = int(input("Introduce el primer numero de la operacion C: "))
Numero_Entero_2 = int(input("Introduce el segundo numero de la operacion C: "))

# Operacion del punto C con el cociente
# Operacion del punto C con el resto
cociente = Numero_1 / Numero_2
resto = Numero_1 % Numero_2

# Resultado de cada operacion
print("Operacion A: ",Operacion_A)
print("Operacion B: ",Operacion_B)
print("Operacion C: "," El cociente: ",cociente,"Resto: ",resto)