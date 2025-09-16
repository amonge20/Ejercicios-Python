# En la competición de skeleton de las olimpiadas de invierno hay tres finalistas. El cronómetro mide
# los siguientes tiempos:
# Hannah Neise: 8 minutos 3 segundos y 10 centésimas
# Jackie Narracott: 12 minutos 7 segundos y 8 centésimas
# Kimberley Bos: 9 minutos 14 segundos y 3 centésimas
# 1. Crea un script que pida los tiempos por pantalla para cada uno de los finalistas
# 2. Convierte los tiempos de minutos-segundos-centésimas a segundos
# 3. Sabiendo que la pista es de 100 metros calcula la velocidad media de cada uno de ellos en
# metros por segundo.
# 4. Imprime los resultados por pantalla

# Punto 1
# Declaracion de las variables
marca_Hannah_Neise = int(0)
marca_Jackie_Narrot = int(0)
marca_Kimberley_Bos = int(0)
pista_metros = int(100)
velocidad_media_Hannah_Neise = float(0.0)
velocidad_media_Jackie_Narrot = float(0.0)
velocidad_media_Kimberley_Bos = float(0.0)

# Preguntamos al comentarista sobre el tiempo que han realizado los competidores
print("\n --- MARCA DE TIEMPO DE HANNAH NEISE ---")
minutos_Hannah_Neise = int(input("¿Minutos?"))
segundos_Hannah_Neise = int(input("¿Segundos?"))
centesimas_Hannah_Neise = int(input("¿Centesimas?"))

print("\n --- MARCA DE TIEMPO DE JACKIE NARROT ---")
minutos_Jackie_Narrot = int(input("¿Minutos?"))
segundos_Jackie_Narrot = int(input("¿Segundos?"))
centesimas_Jackie_Narrot = int(input("¿Centesimas?"))

print("\n --- MARCA DE TIEMPO DE KIMBERLEY BOS ---")
minutos_Kimberley_Bos = int(input("¿Minutos?"))
segundos_Kimberley_Bos = int(input("¿Segundos?"))
centesimas_Kimberley_Bos = int(input("¿Centesimas?"))

# Calculamos el tiempo de los corredores en segundos
marca_Hannah_Neise = (minutos_Hannah_Neise * 60) + segundos_Hannah_Neise + (centesimas_Hannah_Neise / 100)
marca_Jackie_Narrot = (minutos_Jackie_Narrot * 60) + segundos_Jackie_Narrot + (centesimas_Jackie_Narrot / 100)
marca_Kimberley_Bos = (minutos_Kimberley_Bos * 60) + segundos_Kimberley_Bos + (centesimas_Kimberley_Bos / 100)

# La pista es de 100 metros y se calculara la velocidad media de cada uno de los corredores
velocidad_media_Hannah_Neise = pista_metros / marca_Hannah_Neise
velocidad_media_Jackie_Narrot = pista_metros / marca_Jackie_Narrot
velocidad_media_Kimberley_Bos = pista_metros / marca_Kimberley_Bos

# Resultado de los corredores
print('\n --- CLASIFICACIÓN DE LA COMPETICION DE SKELETON ---')
print("Hannah Neise:",minutos_Hannah_Neise,"minutos",segundos_Kimberley_Bos,"segundos","y",centesimas_Hannah_Neise,"centesimas, tiempo en segundos:",marca_Hannah_Neise,"s y velocidad media metro por segundo:",velocidad_media_Hannah_Neise,"m/s")
print("Jackie Narrot:",minutos_Jackie_Narrot,"minutos",segundos_Jackie_Narrot,"segundos","y",centesimas_Jackie_Narrot,"centesimas, tiempo en segundos:",marca_Jackie_Narrot,"s y velocidad media metro por segundo:",velocidad_media_Jackie_Narrot,"m/s")
print("Kimberley Bos:",minutos_Kimberley_Bos,"minutos",segundos_Kimberley_Bos,"segundos","y",centesimas_Kimberley_Bos,"centesimas, tiempo en segundos:",marca_Kimberley_Bos,"s y velocidad media metro por segundo:",velocidad_media_Kimberley_Bos,"m/s")