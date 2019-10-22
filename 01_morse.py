# Escribir un programa que traduzca a código Morse
# Utilizando un diccionario

# Restricciones
#     El programa pedira una línea de texto y la traducirá a morse.
#     El programa seguirá pidiendo líneas hasta que se introduzca una cadena vacía. Entonces dejará de pedir lineas
#     El formato de salida debe ser tal que
#         Se impriman tantas líneas como se han introducido
#         No se imprima nada entre las líneas (controlar la posición del input)

morse = {'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '_.', 'F': '.._.',
         'G': '_ _.', 'H': '....', 'I': '..', 'J': '._ _ _', 'K': '_._', 'L': '._..',
         'M': '_ _', 'N': '_.', 'O': '_ _ _', 'P': '._ _.', 'Q': '_ _ ._', 'R': '._.',
         'S': '...', 'T': '_', 'U': '.._', 'V': '..._', 'W': '._ _', 'X': '_.._',
         'Y': '_._ _', 'Z': '_ _..', '0': '_ _ _ _ _', '1': '._ _ _ _', '2': '.._ _ _',
         '3': '..._ _', '4': '...._', '5': '.....', '6': '_....', '7': '_ _...',
         '8': '_ _ _..', '9': '_ _ _ _.', '.': '·-·-·-', ',': '--··--', ':': '---···',
         '\'': '·----·', '-': '-····-', '/': '-··-·', '(': '-·--·', ')': '-·--·-',
         '"': '·-··-·', '=': '-···-'}


def traducirAMorse(mensaje):
    mensajeMorse = ''
    for caracter in mensaje:
        if caracter in morse:
            mensajeMorse += morse[caracter]
    print(f'{mensajeMorse}')
    return mensajeMorse


# Pedir entrada:
while True:
    mensaje = input('Introduzca el sms que desea telegrafiar: ')
    mensaje = mensaje.upper()
    traducirAMorse(mensaje)
    if mensaje == '' or mensaje == ' ':
        break
