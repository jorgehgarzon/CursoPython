import orden_busqueda as ob
# from orden_busqueda import ordenamiento_insercion
# from orden_busqueda import ordenamiento_burbuja
# from orden_busqueda import busqueda_binaria

lista = [15,3,6,21,4,2,7,0,18,30,0,4,21,34,52,71]

ingresar = input("Desea ingresar una lista? S ó N: ") in ["S","s","Sí","sí","Y","yes","y"]

if ingresar :
    lista = input("Ingrese los elementos separados por comas: ").split(",")

depurar = input("Desea depurar? S ó N: ") in ["S","s","Sí","sí","Y","yes","y"]

print(lista)
lista, contador = ob.ordenamiento_insercion(lista, False, depurar)
print("\nordenada (inserción) descendente: ")
print(lista)
print("contador: ",contador)
lista, contador = ob.ordenamiento_insercion(lista, True, depurar)
print("ordenada (inserción) ascendente: ")
print(lista)
print("contador: ",contador)

lista = [15,3,6,21,4,2,7,0,18,30,0,4,21,34,52,71]
print(lista)
lista, contador = ob.ordenamiento_burbuja(lista, False, depurar)
print("\nordenada (burbuja) descendente: ")
print(lista)
print("contador: ",contador)
lista, contador = ob.ordenamiento_burbuja(lista, True, depurar)
print("ordenada (burbuja) ascendente: ")
print(lista)
print("contador: ",contador)

lista = [15,3,6,21,4,2,7,0,18,30,0,4,21,34,52,71]
print(lista)
lista, contador = ob.ordenamiento_mezcla(lista, False, depurar)
print("\nordenada (mezcla) descendente: ")
print(lista)
print("contador: ",contador)
lista, contador = ob.ordenamiento_mezcla(lista, True, depurar)
print("ordenada (mezcla) ascendente: ")
print(lista)
print("contador: ",contador)

numero = int(input("\nDigite el número que quiere buscar: "))

indice = ob.busqueda_binaria(lista, numero, depurar)
print("La posición es: ",indice)

