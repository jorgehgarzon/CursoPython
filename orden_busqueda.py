def busqueda_binaria(array, valor):
    longitud = len (array)
    centro = longitud/2

    if array[centro] == valor:
        return centro
    elif valor > array[centro]:
        return busqueda_binaria(array[centro+1:], valor) + centro + 1
    else:
        return busqueda_binaria(array[:centro], valor)


def ordenamiento_insercion(array):
    longitud = len(array)

    for i in range (1, longitud):
        elemento = array[i]
        posicion = i -1 

        while posicion > -1 and elemento < array[posicion]:
            array[posicion+1] = array[posicion]
            posicion -= 1

            array[posicion+1] = elemento
    return array

