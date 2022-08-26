def ordenar(lista):
    longitud = len(lista)
    indice_inicial = 0
    indice_final = 0

    for indice_verificar in range (1, longitud):

        elemento = lista[indice_verificar]
        
        posicion = indice_verificar -1
        
        while (posicion > -1) and (elemento < lista[posicion]):
            
            lista[posicion+1]  = lista[posicion]

            posicion-=1

        lista[posicion+1] = elemento   
    return lista    

#lista = [12, 11, 13, 5, 6, 12, 11, 13, 5, 6, -1, 0, -10]
lista = ['Jorge', 'Andres', 'Maria']

ordenar(lista)
print ("Sorted array is:")
for elemento in range(len(lista)):
#	print ("%d" %lista[elemento])
    print (lista[elemento])



