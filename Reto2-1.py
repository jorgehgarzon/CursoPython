

print ("Ingrese la cantidad de productos: ")
prod = int(input())
i = 0
sub = 0


while i < prod:

    cod = int(input("Codigo del producto: "))
    nom = str(input("Nombre al producto: "))
    cant = float(input("Cantidad comprada: "))
    vlr = float(input("Valor unitario (sin IVA): "))
    subprod = cant * vlr
    sub = sub + subprod
    i+=1

iva = sub * 0.19
total = sub + iva    

print("Se vendieron: ", prod, "productos")
print ("subtotal sin IVA: ", sub)
print ("IVA: ", iva)
print ("total con IVA: ", total)









