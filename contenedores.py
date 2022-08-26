#valor - tamaño minimo, tamaño maximo
#100 - 0-1
#250 - >1 - 3.9
#850 - 3.9 - 50

VALOR = 0
TOPE_MINIMO = 1
TOPE_MAXIMO = 2

CONTENEDOR_PEQUENO = (100,0,1)
CONTENEDOR_MEDIANO = (250, 1, 3.8)
CONTENEDOR_GARNDE = (850,3.8,500000)

contador_pequeno=0
contador_mediano = 0
contador_grande = 0


continuar = True

while continuar :
    tamanio =float(input("ingrese tamaño: "))

    if tamanio > CONTENEDOR_PEQUENO[TOPE_MINIMO] and tamanio <= CONTENEDOR_PEQUENO[TOPE_MAXIMO]:
        contador_pequeno+=1
    elif     


