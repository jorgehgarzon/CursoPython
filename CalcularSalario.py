cedula=int(input("ingrese su cedula: "))
salario=float(input("ingrese su salario: "))
desc10=salario * 0.10
desc5=salario * 0.05

if salario > 900000:
    print("para la cedula:", cedula, "su salario: ", salario, "descuento: ", desc10, "salario neto: ", salario - desc10)
else:
    print("para la cedula:", cedula, "su salario: ", salario, "descuento: ", desc5, "salario neto: ", salario - desc5)
