# Calculando la media
# Crear un programa que calcule la media de un conjunto de valores introducido por el usuario.
# Si el usuario entra 0 (cero) será el final de la entrada y se calculara la media.

# Restricciones
#   El cero no se debe incluir en el cálculo de la media
#   Si el primer valor introducido es un cero el programa mostrará un mensaje de error
#   Mantener separadas la entrada, salida y proceso dentro del programa.
#   Si el valor introducido no es numérico volver a pedirlo

# Pedir valores al usuario


def entradaToFloat(valor):
    try:
        resultado = float(valor)
    except:
        resultado = None
    return resultado


total = 0
contador = 0
numero = None

while numero != 0:
    valor = input('Introduce valores para hacer una media: ')
    numero = entradaToFloat(valor)
    while numero == None:
        print('Debes introducir numeros: ')
        valor = input('Introduce valores para hacer una media: ')
        numero = entradaToFloat(valor)
    total += numero
    contador += 1

if contador == 1:
    print('Has introducido un 0 para comenzar, inicia el programa otra vez')
else:
    media = total / (contador - 1)
    print(f'Media = {total} / {contador -1} = {media}')
