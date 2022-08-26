
import  orden_busqueda as lib
from orden_busqueda import ordenamiento_insercion
from orden_busqueda import busqueda_binaria


lista = [1,3,6,4,2,7,0]
print(lista)
lista = lib.ordenamiento_insercion(lista)
print("ordenada: ")
print(lista)

numero = int(input("Digite el numero: "))

indice = lib.busqueda_binaria(lista, numero)
print ("La posicion es: ", indice)

