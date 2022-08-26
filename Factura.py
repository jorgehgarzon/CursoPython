from math import prod


MENU = """
Bienvenido al programa
    1 - Iniciar Pendido 
    2 - Ver factura
    3 - Salir 

Seleccione una opcion: 
"""
SUBMENU = """

Desea ingresar otro producto?
1 - Si
2 - No

"""
productos_pedido =[]

continuar = True

while continuar:
    opcion = int(input(MENU))
    capturar_producto = True
    if opcion == 1:
        while capturar_producto:    
            codigo = int (input("Ingrese codigo:"))
            nombre = input("Ingrese nombre:")
            cantidad = float (input("ingrese cantidad: "))
            valor = float(input("ingrese el valor: "))
            porcentaje_iva = int(input("porcentaje IVBA (0-100): "))
            
            producto = [codigo, nombre, cantidad, valor, porcentaje_iva]
            productos_pedido.append(producto)

            capturar_producto=bool(int(input(SUBMENU)))

    elif opcion==2:
        factura=[]
        for producto_pedido in productos_pedido:
            factura.append(¨[producto_pedido[0],
            factura.append(producto_pedido[1],
            factura.append(producto_pedido[2],
            factura.append(producto_pedido[2]*producto_pedido[3],
            factura.append(producto_pedido[2]*producto_pedido[3] *producto_pedido[3] * producto_pedido[4]/100 )
            subtotal+=(producto_pedido[2]* producto_pedido[3])
            valor_iva+=