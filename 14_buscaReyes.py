# Cuando un rey abdica, su primogénito hereda el trono y debe recibir,
# en su coronación, un número que lo identificará para la posteridad.
# La numeración es importante porque, de otro modo, sería difícil
# diferenciar a reyes con el mismo nombre de una misma dinastía al
# compartir también apellido.

# El resultado es que ante la abdicación de un rey, toca revisar los
# libros de historia para averiguar su número. ¿Eres capaz de hacerlo tú?

# Entrada

# El programa recibirá, por la entrada estándar, múltiples casos de prueba.
# Cada uno consta de una primera línea con un número indicando la cantidad
# de reyes de una determinada dinastía. A continuación vendrá, en otra linea,
# los nombres de todos sus reyes separados por espacio.

# Después aparecerán dos líneas más, una con la cantidad de sucesores futuros
# que hay que numerar (al menos uno), y otra con sus nombres separados por
# espacio.Después aparecerán dos líneas más, una con la cantidad de sucesores
# futuros que hay que numerar (al menos uno), y otra con sus nombres
# separados por espacio.

# Todos los nombres estarán compuestos de una única palabra de no más de 20
# letras del alfabeto inglés, y serán sensibles a mayúsculas. Además, se
# garantiza que en cada caso de prueba no habrá más de 20 nombres de reyes diferentes.

# La entrada acaba con un caso de prueba sin potitos.

# Salida

# Para cada sucesor de cada caso de prueba se indicará, una línea independiente,
# el número que le corresponderá. Aunque normalmente se utilizan números romanos,
# por simplicidad se indicará el número en la notación arábiga tradicional.
# Después de cada caso de prueba se escribirá una línea en blanco.

# Entrada de ejemplo
#   11
#   Felipe Carlos Felipe Felipe Felipe Carlos Felipe Carlos Alfonso Alfonso JuanCarlos
#   3
#   Felipe Leonor Felipe
# Salida de ejemplo
#   6
#   1
#   7


#   12
#   Carlos Isabel Carlos Jorge Jorge Jorge Jorge Guillermo Victoria Jorge Jorge Isabel
#   3
#   Carlos Guillermo Jorge
#   0
# Salida de ejemplo
#   3
#   2
#   7

reyes = ['Felipe', 'Carlos', 'Felipe', 'Felipe', 'Felipe', 'Carlos',
         'Felipe', 'Carlos', 'Alfonso', 'Alfonso', 'JuanCarlos']

sucesorEsp = ['Felipe', 'Leonor', 'Felipe']

kings = ['Carlos', 'Isabel', 'Carlos', 'Jorge', 'Jorge', 'Jorge',
         'Jorge', 'Guillermo', 'Victoria', 'Jorge', 'Jorge', 'Isabel']

sucesorUK = ['Carlos', 'Guillermo', 'Jorge']

numNombresReyes = {}
numNombresSucesores = {}


def mostrarDisnatia(lista):
    for l in lista:
        p = print(f'{l}', end=' ')
    print('\n')
    return p


def nombrePorCoronacion(reyes, sucesores):
    numReyes = len(reyes)
    numSucesores = len(sucesores)

    for r in reyes:
        if r in numNombresReyes:
            numNombresReyes[r] += 1
        else:
            numNombresReyes[r] = 1

    return numReyes, numSucesores, numNombresReyes


def numerosSucesor(sucesores, numNombresReyes):
    for s in sucesores:
        if s in numNombresReyes.keys():
            numNombresReyes[s] += 1
            print(numNombresReyes[s])
            numNombresReyes.get(s)
        else:
            numNombresReyes[s] = 1
            print(numNombresReyes[s])


m = nombrePorCoronacion(reyes, sucesorEsp)
print(m[0])
mostrarDisnatia(reyes)
print(m[1])
mostrarDisnatia(sucesorEsp)
# print('Ver diccionario--> ', m[2])
# print('Ver claves -> ', numNombresReyes.keys())
numerosSucesor(sucesorEsp, numNombresReyes)
# print('Ver diccionario--> ', m[2])
