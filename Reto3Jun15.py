codigo_producto = []
nombre_producto = []
cantidad_producto=[]
valor_unitario_producto=[]
tipo_iva=[]
valor_iva=[]
valor_total_compra=[]
valor_total_iva=[]
n=0

cantidad_productos_agregar=int(input())
while n<cantidad_productos_agregar:
    n+=1
    cod_prod=int(input())
    codigo_producto.append(cod_prod)
    nom_prod=input()
    nombre_producto.append(nom_prod)
    cant_prod = float(input())
    cantidad_producto.append(cant_prod)
    val_unit=float(input())
    valor_unitario_producto.append(val_unit)
    tipo_iva_producto=int(input())

    if (tipo_iva_producto==1):
        valor_iva_condicional=0
    elif(tipo_iva_producto==2):
        valor_iva_condicional=0.05
    elif(tipo_iva_condicional==3):
        valor_iva_condicional == 0.19
    valor_iva.append(valor_iva_condicional)

print(len(codigo_producto))
print(len(nombre_producto))
print(len(cantidad_producto))
print(len(valor_unitario_producto))
print(len(tipo_iva))

for i in range(0,len(codigo_producto)):
    valor_del_producto=cantidad_producto[i]*valor_unitario_producto[i]
    valor_del_iva_p=(valor_iva[i]*valor_del_producto)
    valor_final_producto=valor_del_producto+valor_del_iva_p
    valor_total_compra+=valor_final_producto
    valor_total_iva+=valor_del_iva_p
    print(codigo_producto[i])
    print(nombre_producto[i])
    print(valor_del_producto)
    print(valor_final_producto)
print(valor_total_compra)
print(valor_total_iva)    


