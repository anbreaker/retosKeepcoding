# Una de las técnicas de criptografía más rudimentarias consiste en sustituir cada
# uno de los caracteres por otro situado n posiciones más a la derecha.
# Si n = 2, por ejemplo, sustituiremos la <a> por la <c>, la <b> por la <e>, y así
# sucesivamente.
# El problema que aparece en las últimas n letras del alfabeto tiene fácil solución:
# En el ejemplo, la letra <y> se sustituirá por la <a> y la letra <z> por la <b>.
# La sustitución debe aplicarse a las letras minúsculas, mayúsculas y
# a los dígitos (el <0> se sustituye por el <2>, el <1> por el <3> y así hasta llegar
# al <9>, que se sustituye por el <1>).
# Diseña un programa que lea un texto y el valor de n y muestre su versión criptografiada
# y la versión inversa, que dado un texto y la distancia lo descodifique.
# Ten en cuenta los acentos y mayúsculas.

# abc --> cde

_POSIBLE_VALOR_ENTRADA = 'áéíóúüçÇÁÉÍÓÚ'
_SALIDA = 'aeiouuzZAEIOU'
_ABECEDARIO = 'abcdefghijklmnñoqprstuvwxyz'
_NUMEROS = '0123456789'
textoCrip = ''
descifrado = ''


def convertirAcentos(texto):
    cambiarAcentos = str.maketrans(_POSIBLE_VALOR_ENTRADA, _SALIDA)
    cadena = texto.translate(cambiarAcentos)
    cadena = cadena.lower()
    return texto


def cifrarTexto(texto):
    global textoCrip
    for c in texto:
        indice = _ABECEDARIO.find(c)
        indiceNum = _NUMEROS.find(c)
        if c in _ABECEDARIO or c in _NUMEROS or c == ' ' or c.isascii():
            if indiceNum == 8 or indiceNum == 9:
                textoCrip += _NUMEROS[(indiceNum-8)]
            elif indiceNum != -1:
                textoCrip += _NUMEROS[(indiceNum+2)]
            elif indice == 25 or indice == 26:
                textoCrip += _ABECEDARIO[(indice-25)]
            elif c == ' ':
                textoCrip += ' '
            elif indice != -1:
                textoCrip += _ABECEDARIO[(indice+2)]
            else:
                textoCrip += c
    return textoCrip


def descrifrarTexto(texto):
    global descifrado
    for c in texto:
        indice = _ABECEDARIO.find(c)
        indiceNum = _NUMEROS.find(c)
        if c in _ABECEDARIO or c in _NUMEROS or c == ' ' or c.isascii():
            if indiceNum == 8 or indiceNum == 9:
                descifrado += _NUMEROS[(indiceNum+8)]
            elif indiceNum != -1:
                descifrado += _NUMEROS[(indiceNum-2)]
            elif indice == 0 or indice == 1:
                descifrado += _ABECEDARIO[(indice+25)]
            elif c == ' ':
                descifrado += ' '
            elif indice != -1:
                descifrado += _ABECEDARIO[(indice-2)]
            else:
                descifrado += c
    return descifrado


def validarEntradaOpcion(opcion):
    if opcion != '1' and opcion != '2':
        return False
    else:
        if opcion == '1':
            # Pedir texto
            texto = input('Introduce el texto que desea cifrar: ')
            cifrarTexto(texto.lower())
        else:
            # Pedir texto
            texto = input('Introduce el texto a Descifrar: ')
            descrifrarTexto(texto.lower())
        return True


# Pedir opciones
opcion = input('Elija opcion (Escriba el Nº):\
                  \n\t 1- Cifrar un texto\
                  \n\t 2- Descifrartexto\n\t\t\t\t')
while not validarEntradaOpcion(opcion):
    print('Debe elgir escribiendo el numero que identica la opcion: ')
    opcion = input('Elija opcion (Escriba el Nº):\
                    \n\t 1- Cifrar un texto\
                    \n\t 2- Descifrartexto\n\t\t\t\t')

if textoCrip == '':
    print(f'El Texto Descifrado es: \t\'{descifrado}\'')
if descifrado == '':
    print(f'El Texto cifrado es: \t\'{textoCrip}\'')
