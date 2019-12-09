# Eres un biólogo que examina secuencias de ADN de formas de vida diferentes.
# Se te darán dos secuencias de ADN, y el objetivo es encontrar el conjunto
# ordenado de bases adyacentes de mayor tamaño que es común en ambos ADNs.

# Las secuencias de ADN se darán como conjuntos ordenados de bases de nucleótidos:
# adenina (abreviado A), citosina (C), guanina (G) y timina (T):
#       ATGTCTTCCTCGA TGCTTCCTATGAC

# Para el ejemplo anterior, el resultado es CTTCCT porque que es el conjunto
# ordenado de bases adyacentes de mayor tamaño que se encuentra en ambas formas de vida

# Ejemplo de entrada                                # Salida de la muestra
#       CTGACTGA ACTGAGC                            #       ACTGA
#       CGTAATTGCGAT CGTACAGTAGC                    #       CGTA
#       CTGGGCCTTGAGGAAAACTG GTACCAGTACTGATAGT      #       ACTG

adn1 = 'CTGACTGA'
adn2 = 'ACTGAGC'
adnComun = ''

for b in range(len(adn1)):
    for l in adn2:
        bL = adn1[b]
        cdnAnterior = l
        if adn1[b] == l and adn1 == cdnAnterior:
            adnComun += l
print(adnComun)
