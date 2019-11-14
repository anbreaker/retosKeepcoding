# palos = ['Oro', 'Copa', 'Espada', 'Basto']
# cartas = ['As', '2', '3', '4', '5', '6', '7', 'Sota', 'Caballo', 'Rey']
palos = ['Oro', 'Copa']
cartas = ['As', 'Sota']

baraja = []


def crearBaraja(palos, cartas):
    for palo in palos:
        for numCarta in cartas:
            carta = (f'{numCarta} de {palo}')
            baraja.append(carta)
    return baraja


def barajar(baraja, desplazamiento):
    for c in range(len(baraja)):
        if c < len(baraja):
            copioPosBaraja = baraja.index(baraja[c])
            baraja.remove(baraja[c])
            baraja[desplazamiento] = baraja.append(copioPosBaraja)
    print(baraja)


barajaCreada = crearBaraja(palos, cartas)
print(f'La baraja completa es: {barajaCreada}')

barajada = barajar(baraja, 1)
