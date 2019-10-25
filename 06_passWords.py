import getpass

# Validando contraseñas
# Crear un programa que pida usuario y contraseña y valide si coinciden.
# En caso de coincidir devolver el mensaje:
#        Entró en el sistema
# En el contrario:
#        No te conozco, no pasas
# Lo interesante del programa es datos necesaria para almacenar
# usuarios y sus contraseñas.
# Restricciones:
#     Utilizar if/else
#     Hacer el programa sensible a mayúsculas - minúsculas
# Retos:
#     Impide que la contraseña se vea. Investiga para ello
#     Utiliza un diccionario en lugar de una tupla de tuplas

listaUser = {'anbreaker': 'pass',
             'jessica': 'pass',
             'ramon': 'pass'}


def existeUser(usuario):
    if usuario in listaUser:
        return True
    else:
        return False


# Pedir Usuario
try:
    usuario = input('Introduce nombre usuario: ')
    if listaUser[usuario]:
        print(f'Existe el usuario {usuario}')
        # Pedir contraseña
        passKey = getpass.getpass(prompt='Introduce la contraseña ')
        if passKey.lower() == listaUser.get(usuario):
            print('Puede pasar')
        else:
            print('No puede pasar')
except KeyError:
    print(f'No Existe el usuario {usuario}')
