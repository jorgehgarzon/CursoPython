def busqueda_binaria(array, valor, depurar = False) :
    if depurar :
        print(f"""
                BÚSQUEDA BINARIA 
                Lista = {array}
                Valor = {valor}
            """)
    longitud = len(array)
    centro = longitud//2

    if array[centro] == valor :
        if depurar :
            print(f"""
                    BÚSQUEDA BINARIA 
                    Resultado = {centro}
                """)
        return centro
    elif valor > array[centro] :
        return busqueda_binaria(array[centro+1:], valor) + centro + 1
    else :
        return busqueda_binaria(array[:centro], valor)

def ordenamiento_insercion(array, ascendente = True, depurar = False) :
    if depurar :
        print(f"""
                ORDENAMIENTO POR INSERCIÓN 
                Lista = {array}
                Ascendente = {ascendente}
            """)
    longitud = len(array)
    contador = 0
    for i in range(1, longitud) :
        elemento = array[i]
        posicion = i-1

        while posicion > -1 and (
                (ascendente == True and elemento < array[posicion])
                or (ascendente == False and elemento > array[posicion])
            ) :
            contador += 1
            array[posicion+1] = array[posicion]
            posicion -= 1

        array[posicion+1] = elemento
    if depurar :
        print(f"""
                    ORDENAMIENTO POR INSERCIÓN 
                    Resultado = {array}
                    Contador = {contador}
            """)  
    return array, contador

def ordenamiento_burbuja(array, ascendente = True, depurar = False) :
    if depurar :
        print(f"""
                ORDENAMIENTO BURBUJA 
                Lista = {array}
                Ascendente = {ascendente}
            """)
    longitud = len(array)
    contador = 0
    for i in range(0, longitud-1) :
        for j in range(i+1, longitud) :
            contador += 1
            if (ascendente == True and array[i] > array[j]) or (ascendente == False and array[i] < array[j])  :
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    if depurar :
        print(f"""
                    ORDENAMIENTO BURBUJA 
                    Resultado = {array}
                    Contador = {contador}
            """)                
    return array, contador

def ordenamiento_mezcla(lista, ascendente = True, depurar = False, contador = 0) :
    if depurar :
        print(f"""
                ORDENAMIENTO POR MEZCLA - ** DIVIDIR ** 
                Lista = {lista}
                Ascendente = {ascendente}
                Contador = {contador}
            """)
    contador+=1
    longitud = len(lista)
    if longitud < 2 :
        return lista, 1
    
    centro = longitud//2
    lista_izquierda = lista[:centro]
    lista_derecha = lista[centro:]

    lista_izquierda, contador_izquierda = ordenamiento_mezcla(lista_izquierda, ascendente, depurar, contador)
    lista_derecha, contador_derecha = ordenamiento_mezcla(lista_derecha, ascendente, depurar, contador)

    lista, contador_mezcla = mezclar(lista_izquierda, lista_derecha, ascendente, depurar)
    contador += (contador_mezcla + contador_izquierda + contador_derecha)
    if depurar :
        print(f"""
                    ORDENAMIENTO POR MEZCLA - ** DIVIDIR **
                    Resultado = {lista}
                    Contador Recursión + Iteraciones = {contador}
            """)  
    return lista, contador
    
def mezclar(izquierda, derecha, ascendente, depurar = False) :  
    if depurar :
        print(f"""
                ORDENAMIENTO POR MEZCLA - ** MEZCLAR **
                Izquierda = {izquierda}
                Derecha = {derecha}
                Ascendente = {ascendente}
            """)  
    contador_mezcla = 0
    lista_ordenada = []
    while len(izquierda) > 0 and len(derecha) > 0 :
            contador_mezcla += 1
            if (ascendente == True and izquierda[-1] < derecha[0]) or (ascendente==False and  izquierda[-1] > derecha[0]):
                lista_ordenada = lista_ordenada + izquierda + derecha
                break
            elif (ascendente and izquierda[0] > derecha[-1]) or ((not ascendente) and izquierda[0] < derecha[-1])  :
                lista_ordenada = lista_ordenada + derecha + izquierda
                break
            else :
                if (ascendente and izquierda[0] < derecha[0]) or ((not ascendente) and izquierda[0] > derecha[0]) :
                    lista_ordenada.append(izquierda.pop(0))
                else :
                    lista_ordenada.append(derecha.pop(0))

    if depurar :
        print(f"""
                    ORDENAMIENTO POR MEZCLA - ** MEZCLAR **
                    Resultado = {lista_ordenada}
                    Contador Iteraciones = {contador_mezcla}
            """)  
    return lista_ordenada, contador_mezcla
