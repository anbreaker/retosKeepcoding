# Lenguaje pi Reglas de silabeo en español
# vF                - La sílaba más pequeña se forma por una vocal.
# vF - vF           - Dos vocales se separan, si las dos son fuertes.
# vFvD y vDvD 	    - Dos vocales no se separan si una es fuerte y la otra es débil, ni si las dos son débiles.
# cV                - La sílaba más común en el español es la que se forma con una consonante seguida por una vocal.
# C - C             - Dos consonantes juntas normalmente se separan
# CC / c = lr   	- Dos consonantes juntas se mantienen juntas si la segunda es una /l/ o /r/.
# CC / = ch, ll, rr - Dos consonantes juntas se mantienen juntas si representan los sonidos [ch], [ll] o [rr].
# C - CC            - Tres consonantes juntas, la primera se separa de las otras dos.
# CC-C / CsC        - Tres consonantes juntas, las primeras dos se separan de la última si la del medio es una /s/
# CC - CC           - Cuatro consonantes juntas, se dividen por la mitad.


# Tipos:  c -> Consonante
#        pC -> parConsonantes
#        vA -> vocalesAbiertasFuertes
#        vC -> vocalesCerradasDebiles
#        sV -> semiVocales

c = ['b', 'c', 'd' 'f', 'g', 'h', 'j', 'k', 'l', 'm',
     'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
pC = ['bl', 'cl', 'fl', 'gl', 'kl', 'pl', 'tl', 'br',
                  'cr', 'dr', 'fr', 'gr', 'kr', 'pr', 'tr', 'ch', 'll', 'rr']
vF = ['a', 'e', 'o', 'á', 'é', 'ó', 'ú']
vD = ['i', 'u', 'ü']
sV = ['y']


listaPalabras = []
silabas = []
tipos = []

# fraseTransformada --> 'pihopila pimunpido'

frase = 'Blanco'
listaPalabras = frase.lower().split(' ')


for palabra in listaPalabras:
    for letra in palabra:
        if letra in vF:
            tipos.append('vF')
        elif letra in vD:
            tipos.append('vD')
        elif letra in c:
            tipos.append('c')
    tipos.append(' ')

if tipos[-1] == ' ':
    tipos.pop()


print(tipos)
print(tipos.reverse())
