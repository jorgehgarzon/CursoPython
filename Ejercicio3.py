UN_LITRO = 100
MAS_LITRO = 250
GALON = 800

contenedor1 = int(input("ingrese el primer contenedor: "))


if contenedor1 < UN_LITRO: 
    print ("el contenedor 1 es igual o menor a un litro ", contenedor1)

elif contenedor1 > MAS_LITRO and contenedor1 < GALON:
    print ("el contenedor 1 es mayor a un litro pero menor de un galon ", contenedor1)

if contenedor1 >= GALON:
    print ("el contenedor 1 es igual o mayor a un galon ", contenedor1)
