# Eres un biólogo que examina secuencias de ADN de formas de vida diferentes.
# Se te darán dos secuencias de ADN, y el objetivo es encontrar el conjunto
# ordenado de bases adyacentes de mayor tamaño que es común en ambos ADNs.

# Las secuencias de ADN se darán como conjuntos ordenados de bases de nucleótidos:
# adenina (abreviado A), citosina (C), guanina (G) y timina (T):
#       ATGTCTTCCTCGA TGCTTCCTATGAC

# Para el ejemplo anterior, el resultado es CTTCCT porque que es el conjunto
# ordenado de bases adyacentes de mayor tamaño que se encuentra en ambas formas de vida

# Ejemplo de entrada                                # Salida de la muestra
#       CTGACTGA                ACTGAGC             #       ACTGA
#       CGTAATTGCGAT            CGTACAGTAGC         #       CGTA
#       CTGGGCCTTGAGGAAAACTG    GTACCAGTACTGATAGT   #       ACTG

adn1 = 'CTGACTGA'
adn2 = 'ACTGAGC'
cadenaLarga = ''

i1 = 1
i2 = 0
while i1 < len(adn1):
    while i2 < len(adn2):
        if adn1[i1] == adn2[i2]:
            cadenaLarga += adn1[i1]

    else:
