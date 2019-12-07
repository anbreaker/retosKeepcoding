# Escribir un programa que traduzca a código Morse
# Utilizando un diccionario

# Restricciones
#     El programa pedira una línea de texto y la traducirá a morse.
#     El programa seguirá pidiendo líneas hasta que se introduzca una cadena vacía. Entonces dejará de pedir lineas
#     El formato de salida debe ser tal que
#         Se impriman tantas líneas como se han introducido
#         No se imprima nada entre las líneas (controlar la posición del input)

morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
         'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..', ' ': '/', '0': '-----', '1': '.----', '2': '..---',
         '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
         '8': '---..', '9': '----.', '.': '·-·-·-', ',': '--··--', ':': '---···',
         '\'': '·----·', '-': '-····-', '/': '-··-·', '(': '-·--·', ')': '-·--·-',
         '"': '·-··-·', '=': '-···-'}


def traducirAMorse(mensaje):
    mensajeMorse = ''
    for caracter in mensaje:
        if caracter not in morse:
            mensajeMorse += '{X}'
        else:
            mensajeMorse += morse[caracter] + ' '
    print(f'{mensajeMorse}')
    return mensajeMorse


# Pedir entrada:
while True:
    mensaje = input('Introduzca el sms que desea telegrafiar: ')
    mensaje = mensaje.upper()
    traducirAMorse(mensaje)
    if mensaje == '' or mensaje == ' ':
        print('Hasta la proxima')
        break
