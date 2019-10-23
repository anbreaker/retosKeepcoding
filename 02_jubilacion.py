from datetime import datetime

# Cálculo de la jubilación
# Incorpora el año actual al programa.
# Crea un programa que cuente cuantos años faltan para tu jubilación y que te diga el año en que te jubilarás.
# Algo así:
#     ¿Cuantos años tienes? 48
#     ¿A qué edad te jubilarás? 67
#     Te quedan 19 años para jubilarte
#     Estamos en 2018, te jubilarás en 2037.
# Restricciones
#     Convertir las cadenas de entrada en números
#     Obten el año actual como lo haga python (no vale ponerlo como constante en el programa)
# Reto
#     Maneja la situación si el programa devuelve un número negativo de modo que diga que ya puede jubilarse

current_data = datetime.now()
year = str(current_data.year)


def validarEdad(edad):
    if edad > 0:
        return True
    else:
        return False


def tiempoHastaJubilacion(edad, jubilacion):
    tiempoHastaJubilacion = int(jubilacion - edad)
    yearJubilacion = year(year+tiempoHastaJubilacion)
    print(f'año jubliacion--> {yearJubilacion}')
    return(tiempoHastaJubilacion)


# Pedir edad
while True:
    try:
        edad = int(input('¿Cuantos años tienes?: '))
    except ValueError:
        print('Debes introducir una edad numérica y positiva. ')
    else:
        if not validarEdad(edad):
            print('Debes introducir una edad numérica y positiva. ')
        else:
            break


# Pedir edad de jubilacion
while True:
    try:
        jubilacion = int(input('¿A qué edad te jubilas? '))
    except ValueError:
        print('Debes introducir una edad numérica y positiva. ')
    else:
        if not validarEdad(jubilacion):
            print('Debes introducir una edad numérica y positiva. ')
        else:
            break


faltan = tiempoHastaJubilacion(edad, jubilacion)
print(
    f'Estamos en {year} tienes {edad} años, te vas a jubilar con {jubilacion} y te quedan {faltan}')
