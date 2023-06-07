#1 cuenta regresiva
def contador(num):
    for i in range(num,0,-1):
        print(i)
contador(5)

#2 imprimir y devolver una lista
def imp_devolver(lista):
    print(lista[0])
    return lista[1]

devolver = imp_devolver([4,3])
print(devolver)

#3primero más longitud
def longitud(sum_lista):
    long= len(sum_lista)
    print(sum_lista[0] + long)

longitud([1,2,3,4,5])

#4 valores mayores que el segundo
def mayor(lista):
    segundo_valor = lista[1]
    lista_dos=[]
    for i in range(len(lista)):
        if lista[i]>segundo_valor:
            lista_dos.append(lista[i])
    return lista_dos

print(mayor([5,2,3,2,1,4]))

#5 Esta longitud, este valor
def longitud_valor(longitud,valor):
    segunda_lista = []
    for i in range(longitud):
        segunda_lista.append(valor)
    return segunda_lista

print(longitud_valor(6,2))

