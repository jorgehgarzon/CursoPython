prod = int(input("Ingrese la cantidad de productos: "))
i=0
sub=0
total = 0
subiva=0
totaliva = 0

EXENTO = 0
BIENES = 0.05
GENERAL = 0.19

while i<prod:
    cod = int(input("Codigo del producto: "))
    nom = input("Nombre del producto: ")
    cant = float(input("Ingrese la cantidad: "))
    vlr = float(input("Valor sin IVA:"))
    iva = int(input("Ingrese IVA: 1-sin IVA, 2 - IVA del 5%, 3 - IVA del 19%: "))
    if iva == 1:
        subtotal = (vlr * cant) * EXENTO
        subiva = subtotal + subiva
        totalprd = subtotal + subiva
    elif iva == 2:
        subtotal  = (vlr * cant) * BIENES
        subiva = subtotal + subiva
        totalprd = subtotal + subiva
        
    elif iva == 3:
        subtotal  = (vlr * cant) * GENERAL 
        subiva = subtotal + subiva
        totalprd = subtotal + subiva
    print ("Codigo del producto: ", cod)
    print ("Nombre del producto: ", nom)
    print ("Cantidad comprada: ", prod)
    print ("Valor producto: ", subtotal)    
    sub=sub+totalprd
    subiva = subiva + iva
    i+=1
total = totalprd
totaliva = subiva
print ("Valor total con IVA: ", total)
print("Valor del IVA: ", totaliva) 
