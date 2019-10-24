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

listaUser = {'anbreaker': 'anbreakerPass',
             'jessica': 'jessicaPass',
             'ramon': 'ramonPass'}

usuario = input('Introduce nombre usuario: ')


try:
    if listaUser[usuario]:
        print(f'Existe el usuario {usuario}')
        password = input('Introduce tu contraseña: ')
        if listaUser.get(usuario) == password:
            print('Puede pasar')
        else:
            print('No puede pasar')
except KeyError:
    print(f'No Existe el usuario {usuario}')
