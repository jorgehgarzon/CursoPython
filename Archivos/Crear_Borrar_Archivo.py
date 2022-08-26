
import os

try:
    archivo=open("C:\\Users\\jorge.garzon\\Downloads\\Ejercicios\\Listado.txt")
    lista = archivo.readlines()
    print(lista)
    archivo.close
    print("pasa")
except FileNotFoundError:
    print("No existe el archivo!!")    


archivo = open(r"C:\Users\jorge.garzon\Downloads\Ejercicios\Archivos\Productos\Listado10.txt", "x")   
archivo.write("nuevo archivo")
archivo.close()

os.remove(r"C:\Users\jorge.garzon\Downloads\Ejercicios\Archivos\Productos\Listado10.txt")
