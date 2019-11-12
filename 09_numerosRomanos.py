# Conversor de numeros romanos en python
# I	1	|   V	5	|   X	10
# L	50	|   C	100	|   D	500 | M	1000

# valoresNumerosRomanos = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

numRomanos = {'M': 1000, 'CM': 900, 'D': 500, 'C': 100,
              'XC': 90, 'L': 50, 'X': 10, 'IX': 9, 'V': 5, 'I': 1}


def descomponiendoNumArabigo(numero):  # Convertir a romano:
    resultado = ''
    for item in numRomanos:
        cociente = numero // numRomanos.get(item)
        if cociente > 0:
            numero = numero - numRomanos.get(item)*cociente
            mayorTres = item*cociente
            if mayorTres == 'CCCC':
                resultado += 'CD'
            elif mayorTres == 'XXXX':
                resultado += 'XL'
            elif mayorTres == 'IIII':
                resultado += 'IV'
            else:
                resultado += mayorTres
            print(
                f'Letra Romana {item}\'s--> {cociente}\t num Arabe--> {numRomanos.get(item)}')
    # print(f'Resultado al final --> {resultado}')
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


# numero = 3999

print(f'El numero {numero} en romano es: {descomponiendoNumArabigo(numero)}')
