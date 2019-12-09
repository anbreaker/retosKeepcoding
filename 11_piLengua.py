# Lenguaje pi Reglas de silabeo en español
# V v               - La sílaba más pequeña se forma por una vocal.
# V - V             - Dos vocales se separan, si las dos son fuertes.
# Vv y vv 	        - Dos vocales no se separan si una es fuerte y la otra es débil, ni si las dos son débiles.
# cV o cv           - La sílaba más común en el español es la que se forma con una consonante seguida por una vocal.
# C - C             - Dos consonantes juntas normalmente se separan
# CC / c = lr   	- Dos consonantes juntas se mantienen juntas si la segunda es una /l/ o /r/.
# CC / = ch, ll, rr - Dos consonantes juntas se mantienen juntas si representan los sonidos [ch], [ll] o [rr].
# C - CC            - Tres consonantes juntas, la primera se separa de las otras dos.
# CC-C / CsC        - Tres consonantes juntas, las primeras dos se separan de la última si la del medio es una /s/
# CC - CC           - Cuatro consonantes juntas, se dividen por la mitad.


# Tipos:  c -> Consonante
#        C -> parConsonantes
#        V -> vocalesAbiertasFuertes
#        v -> vocalesCerradasDebiles
#        s -> semiVocales

c = ['b', 'c', 'd' 'f', 'g', 'h', 'j', 'k', 'l', 'm',
     'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
C = ['bl', 'cl', 'fl', 'gl', 'kl', 'pl', 'tl', 'br',
     'cr', 'dr', 'fr', 'gr', 'kr', 'pr', 'tr', 'ch', 'll', 'rr']
V = ['a', 'e', 'o', 'á', 'é', 'ó', 'ú']
v = ['i', 'u', 'ü']
s = ['y']

norma = {'ccV': ' '}

# V v
# V - V
# Vv y vv
# cV o cv
# C - C
# CC / c = lr
# CC / = ch, ll, rr
# C - CC
# CC-C / CsC
# CC - CC

listaPalabras = []
silabas = []
tipos = ''

# fraseTransformada --> 'pihopila pimunpido'

frase = 'Blanco'
listaPalabras = frase.lower().split(' ')


for palabra in listaPalabras:
    for letra in palabra:
        if letra in V:
            tipos += 'V'
        elif letra in v:
            tipos += 'v'
        elif letra in c:
            tipos += 'c'
    tipos += ' '


print(tipos)
