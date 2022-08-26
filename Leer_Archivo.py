
try:
    archivo=open("C:\\Users\\jorge.garzon\\Downloads\\Ejercicios\\Listado.txt")
    print(archivo.read())
    archivo.close
except FileNotFoundError:
    print("No existe el archivo!!")    