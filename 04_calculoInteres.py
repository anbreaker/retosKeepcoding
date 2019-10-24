# Cálculo de interés simple
# Crear un programa que calcule el interés simple, teniendo en cuenta que se calcula
# con la siguiente fórmula:
#     A=P⋅(1+rt)
#     Donde A es la cantidad ganada, P la cantidad invertida,
#     r el interes y t los años transcurridos desde el inicio de la inversión
#     Tras t años de inversión al r %, su cantidad debe ser A
# Restricciones
#     La tasa de interés debe introducirse como porcentaje y no decimal,
#     es decir 15 y no 0,15
#     La inversión debe redondearse al céntimo
#     La salida debe formatearse como divisa (€)
# Retos
#     Valida que las entradas sean numéricas y que el usuario no pueda
#     continuar si no introduce un número
#     Modifica el programa para que imprima el valor de la inversión cada
#     año de la misma hasta llegar al valor pedido


def validarCantidad(cantidad):
    if cantidad > 0:
        return True
    else:
        return False


# Pedir entrada de datos
while True:
    try:
        cantidadInvertir = float(input('Introduce Cantidad a invertir: '))
        cantidadInvertir = round(float(cantidadInvertir, 2))
        tasaInteres = float(input('Introduce tasa de interes: '))
    except ValueError:
        print('Debes introducir sólo numéros. ')
    else:
        if not validarCantidad(tasaInteres):
            print('Debes introducir numéros positivos. ')
        else:
            break

'''
strQ = input("Cantidad invertida: ")
strA = input("Años transcurridos: ")
strI = input("Interés anual: ")

Q = round(float(strQ), 2)
A = float(strA)
I = float(strI)/100

ganancia = Q * (1 + I * A)

print("Tras {} años de inversión al {:.2f}%, su cantidad debe ser {:.2f}€".format(
    A, I*100, ganancia))
'''
