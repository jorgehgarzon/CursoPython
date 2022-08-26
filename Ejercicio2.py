import string
longitud = float(input("ingrese la longitud del campo en pies: "))
ancho = float(input("ingrese el ancho del campo en pies: "))
area_pies = longitud * ancho
ACRE = 43560
area_acres = area_pies/ACRE

print ("El area del campo en acres es: ", area_acres)
