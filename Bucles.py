#lista = ["Jorge", "Humberto", "Garzon", "Salazar"]

#for n in lista:
#    print(n)


def pedirNumeroEntero():

    correcto=False
    num=0
    while(not correcto):
        try:
            num=int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print("Error, introduce un numero entero")
    return num            

salir = False
opcion = 0

while not salir:
    print ("1. Opción 1 ")    
    print ("2. Opción 2 ")    
    print ("3. Opción 3 ")    
    print ("4. Salir ")    

    print ("Elige una opción..")
    opcion = pedirNumeroEntero()

    if opcion == 1:
        print("Opcion 1")
    elif opcion == 2:
        print ("Opcion 2")
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")       

    print("fin!!")             