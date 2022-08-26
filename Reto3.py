codigo_producto=[]
nombre_producto=[]
cantidad_producto=[]
valor_unitario_producto=[]
tipo_iva=[]
valor_iva=[]
valor_total_de_la_compra=0
valor_total_del_iva=0
n=0
# N, como la cantidad de productos a procesar.
cantidad_productos_agregar=int(input())
while n<cantidad_productos_agregar:
    n+=1
    cod_prod=int(input())
    codigo_producto.append(cod_prod)
    nom_prod=input()
    nombre_producto.append(nom_prod)
    cant_prod=float(input())
    cantidad_producto.append(cant_prod)
    val_unit=float(input())
    valor_unitario_producto.append(val_unit)
    tipo_iva_producto=int(input())
    tipo_iva.append(tipo_iva_producto)
    
    if(tipo_iva_producto==1):
       valor_iva_condicional= 0
      
    elif(tipo_iva_producto==2):
        valor_iva_condicional=0.05   
             
    elif(tipo_iva_producto==3):
        valor_iva_condicional= 0.19
    valor_iva.append(valor_iva_condicional)
    
# la longitud de la lista de códigos
print(len(codigo_producto))
# longitud de la lista de nombres
print(len(nombre_producto))
# longitud de la lista de cantidad comprada
print(len(cantidad_producto))
# longitud de la lista de valor unitario 
print(len(valor_unitario_producto))
# la longitud de la lista de tipo de IVA
print(len(tipo_iva))

for i in range(0,len(codigo_producto)):
    
    valor_del_producto=cantidad_producto[i]*valor_unitario_producto[i]
    
    valor_del_iva_p=(valor_iva[i]*valor_del_producto)
    
    valor_final_p roducto=valor_del_producto+valor_del_iva_p
    
    valor_total_de_la_compra+=valor_final_producto
    
    valor_total_del_iva+=valor_del_iva_p
    
    print(codigo_producto[i])
    print(nombre_producto[i])
    print(valor_del_producto)
    print(valor_final_producto)
    
print(valor_total_de_la_compra)
print(valor_total_del_iva)