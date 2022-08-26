IMPUESTO=0.19
propina=0

error = True
costos=[]
i=0
total=0
for i in range(0,3):
    while error:
        try:
            costo=float(input("Costo de la comida:"))
            costos.append(costo)
            total=total+costos[i]
        assert(costo>0)
    error=False
   except ValueError:
    print("El costo de la comida debe ser numérico.")
    except AssertionError:
    print("El costo de la comida debe ser mayor a cero.")
    error = True

while error:
    try:
        nivel=int(input("Nivel de satisfacción: 1: muy satisfecho; 2: satisfecho; 3: insatisfecho : "))
        assert(nivel==1 or nivel==2 or nivel==3)
    error=False
    except ValueError:
    print("El nivel de satisfacción debe ser numérico.")
    except AssertionError:
    print("El nivel de satisfacción debe ser 1, 2 o 3.")

if nivel==1:
    propina=0.14
if nivel==2:
    propina=0.10
if nivel==3:
    propina=0.05

cuenta=total*(1+IMPUESTO+propina)
print ("La cuenta total es:",cuenta)
