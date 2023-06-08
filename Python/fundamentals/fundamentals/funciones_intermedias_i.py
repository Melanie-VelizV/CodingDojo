#Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ] 
def cambiar_valor(x):
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i][j]==10:
                x[i][j] = 15
cambiar_valor(x)
print(x)


#Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

def cambiar_apellido(estudiantes):
    for i in estudiantes:
        if i['last_name'] == 'Jordan':
            i['last_name'] = 'Bryant'

cambiar_apellido(estudiantes)
print(estudiantes)


#En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}

def cambiar_nombre(directorio_deportes):
    if 'fútbol' in directorio_deportes:
        jugadores = directorio_deportes['fútbol']
        for i in range(len(jugadores)):
            if jugadores[i] == 'Messi':
                jugadores[i] = 'Andrés'

cambiar_nombre(directorio_deportes)
print(directorio_deportes)


#Cambia el valor 20 en z a 30.
z = [ {'x': 10, 'y': 20} ]
def cambiar_y(z):
    for i in z:
        if i['y'] == 20:
            i['y'] = 30

cambiar_y(z)
print (z)