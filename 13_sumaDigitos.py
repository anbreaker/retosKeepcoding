# Se trata de implementar un programa que sume los dígitos de un número entero no negativo.
#           Ejemplo, la suma de los dígitos del 3433 es 13.

# El programa no se limitará a escribir el resultado dela suma, sino también escribirá
# los sumandos utilizados: 3 + 4 + 3 + 3 = 13.

# Entrada

# La entrada consta de una serie de casos de prueba terminados con un número negativo.
# Cada caso de prueba es una simple línea con un número no negativo no mayor que 10⁹
# del que habrá que sumar todos sus dígitos.

# Salida

# Para cada caso de prueba se mostrará una línea en la que aparecerán cada uno de los dígitos
# separados por el signo +, tras lo cual aparecerá el símbolo = y la suma de todos los dígitos.

# Ten en cuenta que antes y después de cada símbolo(+ e =) hay un espacio.

# Nota: el programa no debe avisar al usuario con mensajes como "Introduzca un número".
# Debe leer directamente el número que introduzca el usuario y la respuesta debe ser exactamente
# como aparece aquí explicado y como se puede comprobar en el ejemplo.
# http://www.nachocabanes.com/retos/reto.php?n=024

numero = 34331
numeroStr = str(numero)
resultado = ''
suma = 0
for pos in range(len(numeroStr)):
    suma += int(numeroStr[pos])
    if pos < (len(numeroStr)-1):
        resultado += f'{numeroStr[pos]} + '
    else:
        resultado += numeroStr[pos]


print(f'{resultado} = {suma}')
