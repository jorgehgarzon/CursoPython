
try:
    archivo=open(r"C:\\Users\\jorge.garzon\\Downloads\\Ejercicios\\Listado.txt", "r")
    contenido = archivo.readlines()
    print(contenido)
    archivo.close
    print("pasa")
except FileNotFoundError:
    print("No existe el archivo!!")  