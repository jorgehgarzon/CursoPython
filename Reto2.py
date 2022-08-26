cantidad = int(input("ingrese la cantidad de productos a procesar: "))
codigo = int(input("ingrese el codigo del producto: "))
nombre = str(input("Ingrese el nombre del producto: "))
cantidad_comprada = float(input("Ingrese la cantidad comprada del producto: "))
valor_unitario = float(input("Ingrese el valor unitario del producto (sin IVA): "))
tipo_IVA = int(input("1 - Exento de IVA, 2 - Bienes 5%, 3 - general 19%: "))

valorT_sinIVA = cantidad_comprada * valor_unitario
valorT_IVA5 = (cantidad_comprada * valor_unitario)*1.05
valorT_IVA19 = (cantidad_comprada * valor_unitario)*1.19

if tipo_IVA == 1:
    print("Producto Exento de IVA!!")
    print("codigo producto: ", codigo, "nombre: ", nombre, "valor sin IVA: ", valor_unitario, "valor final: ", valorT_sinIVA)

elif tipo_IVA == 2:
    print(" Su producto es un bien y se aplicará el 5% ")
    print("codigo producto: ", codigo, "nombre: ", nombre, "valor sin IVA: ", valor_unitario, "valor final: ", valorT_IVA5)

elif tipo_IVA == 3:    
    print("su producto tiene el 19% de IVA")
    print("codigo producto: ", codigo, "nombre: ", nombre, "valor sin IVA: ", valor_unitario, "valor final: ", valorT_IVA19)

else: 
    print("opción erronea, seleccione la opción correcta")
    exit



