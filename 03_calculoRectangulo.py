# Area de un rectángulo
# Pide la entrada del ancho y largo de la habitación en metros.
# Devuelve la superficie en metros cuadrados y en yardas cuadradas.
# (1 metro cuadrado son 1.19599 yardas cuadradas).

# Restricciones
#     Mantener los cálculos separados de la salida.
#     Usa una constante para las conversiones de unidades.isalpha()
# Retos
#     Fuerza a que las entradas sean numéricas. Si no son numericas
#     el usuario no podrá continuar.
#     Crea una versión del programa que permita elegir si la entrada
#     va en metros o en yardas


def validarMedida(medida):
    if medida > 0:
        # print(f'en la def {medida}')
        return True
    else:
        return False


def calculoMetrosCuadrados(ancho, alto):
    superficieMetros = ancho * alto
    return superficieMetros


def calculoYardasCuadradas(superficieMetros):
    superficieYardas = superficieMetros * 1.19599
    return superficieYardas


# Pedir entrada de datos
while True:
    try:
        ancho = int(input('Ancho de la habitacion: '))
        alto = int(input('Largo de la habitacion: '))
    except ValueError:
        print('Debes introducir sólo numéros. ')
    else:
        if not validarMedida(ancho) or not validarMedida(alto):
            print('Debes introducir numéros positivos. ')
        else:
            break

superficieM = calculoMetrosCuadrados(ancho, alto)
superficieY = calculoYardasCuadradas(superficieM)

print(f'La superficie en m² es: {superficieM}')
print(f'La superficie en yardas² es: {superficieY}')
