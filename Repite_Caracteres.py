# Crea un script que acepte un string de 5 caracteres y devuelva otro string con todos los caracteres
# duplicados. Si el input es ‘sbc56’, el output deberá ser ‘ssbbcc5566’

# Funcion para duplicar los caracteres
def duplicar_caracteres(texto):
    texto_duplicado = ""
    for caracter in texto:
        texto_duplicado += caracter * 2
    return texto_duplicado

# Preguntamos al usuario el numero de caracteres que quiere poner (Que son 5)
print("Introduce como máximo 5 caracteres:")
caracteres = input()
resultado_caracteres = duplicar_caracteres(caracteres)

# Mostramos el resultado final con los caracteres duplicados
print(resultado_caracteres)