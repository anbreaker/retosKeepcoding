palos = ['oro', 'copa', 'espada', 'basto']
cartas = ['As', '2', '3', '4', '5', '6', '7', 'Sota', 'Caballo', 'Rey']
baraja = []


def crearBaraja(palos, cartas):
    for palo in palos:
        for numCarta in cartas:
            carta = (f'{numCarta[0]}.{palo[0]}')
            baraja.append(carta)
    return baraja


def barajar(baraja, desplazamiento):
    for i in range(len(baraja)):
        valor = baraja[i]
        baraja.remove(valor)
        baraja.insert(desplazamiento, valor)
    return baraja


barajaCreada = crearBaraja(palos, cartas)
print(f'Baraja Comepleta:\n\n{barajaCreada}\n\n')

barajar = barajar(baraja, 19)
print(barajar)
