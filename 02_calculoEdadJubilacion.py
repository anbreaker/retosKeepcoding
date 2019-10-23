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

_FORMATO_FECHA = "%d-%m-%Y"
_CURRENT_DATA = datetime.now().date()


def validarFecha(cadena):
    try:
        datetimeObject = datetime.strptime(cadena, _FORMATO_FECHA)
        if str(datetimeObject) > str(_CURRENT_DATA):
            print('\n\tDebes al menos haber nacido ;)\n')
            return False
        elif datetimeObject.year < 1910:
            print('¿Seguro que sigues vivo? ;)')
            return False
        return True
    except ValueError:
        return False


# Pedir fecha
fecha = input('Dime tu fecha de nacimiento (dd-mm-yyyy): ')
while not validarFecha(fecha):
    print('Debes introducir una fecha correcta, con el formato dd-mm-yyyy')
    fecha = input('Dime tu fecha de nacimiento (dd-mm-yyyy): ')
