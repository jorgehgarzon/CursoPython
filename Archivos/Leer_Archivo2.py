
import json

def mostrar_producto():
    archivo=open(r"C:\Users\jorge.garzon\Downloads\Ejercicios\Archivos\Listado1.json", "r")
    contenido = archivo.read()
    lista_productos= json.loads(contenido)
    print(lista_productos)
    archivo.close
    return lista_productos


def agregar_producto():
    lista = mostrar_producto()
    archivo = open(r"C:\Users\jorge.garzon\Downloads\Ejercicios\Archivos\Listado1.json", "wt")
    codigo = input("ingrese codigo: ")
    producto = input("ingrese producto: ")
    valor = input("ingrese valor: ")
    productos = {"codigo": int(codigo), "producto": producto, "valor": float(valor) }
    lista.append(productos)
    contenido = json.dumps(lista)
    archivo.write(contenido)
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
        print(mostrar_producto())
    else:
        continuar = False        
