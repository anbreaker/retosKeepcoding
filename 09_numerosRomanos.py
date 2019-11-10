# Conversor de numeros romanos en python
# I	1	|   V	5	|   X	10
# L	50	|   C	100	|   D	500 | M	1000

numRomanos = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
numRomanos2 = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}


def descomponiendoNumArabigo(numero):  # Convertir a romano:
    resultado = ''
    for item in numRomanos:
        des = numero // numRomanos.get(item)

        if des > 0:
            resultado += item
            print(
                f'Letra Romana {item}\'s--> {des}\t num Arabe--> {numRomanos.get(item)}')


def numToRoman(numero):
    resultado = ''
    if numero < 4:
        for i in range(numero):
            resultado += numRomanos2.get(1)
    return resultado


def validarNumero(numero):
    if numero > 0:
        # print(f'en la def {numero}')
        return True
    else:
        return False


# Pedir opciones
numero = 0
while not validarNumero(numero):
    try:
        if not validarNumero(numero):
            numero = int(input('Introduzca un numero entero: '))
    except ValueError:
        print('Debes introducir sólo numéros enteros positivos. ')


# print(f'El numero {numero} en romano es: {numToRoman(numero)}')
print(f'El numero {numero} en romano es: {descomponiendoNumArabigo(numero)}')
