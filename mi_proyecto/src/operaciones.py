def filtrar_pares(lista):
    '''Recibe una lista y devuelve una nueva con los números pares.'''
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
    return pares
