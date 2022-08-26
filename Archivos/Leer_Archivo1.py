
import json

def mostrar_producto():
    archivo=open(r"C:\Users\jorge.garzon\Downloads\Ejercicios\Archivos\Listado1.json", "r")
    contenido = archivo.read()
    lista_productos= json.loads(contenido)
    print(lista_productos)
    archivo.close


def agregar_producto():
    archivo = open(r"C:\Users\jorge.garzon\Downloads\Ejercicios\Archivos\Productos\Listado.txt", "at")
    codigo = input("ingrese producto: ")
    nombre = input("ingrese nombre: ")
    valor = input("ingrese valor: ")
    line = "\n" + codigo + "," + nombre + "," + valor
    archivo.write(line)
    archivo.close()

MENU = """  
    Que desea hacer?

    1. Agregar productos
    2. Mostrar productos
    3. No hacer nada mas
"""        
continuar = True
while continuar:
    print(MENU)
    opcion = int(input("ingrese opcion: "))
    if opcion == 1:
        agregar_producto()
    elif opcion == 2:
        mostrar_producto()
    else:
        continuar = False        
