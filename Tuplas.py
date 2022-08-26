

VOCALES = ["a", "e", "i", "o", "u"]

texto = input("Digite las palabras:")

palabras = texto.split(" ")
resultados =[]

for palabra in palabras:
    termina = palabra[-1]
    if termina in VOCALES:
        plural = palabra + "s"
    else:
        plural = palabra + "es"    

    tupla_plural = (palabra, plural)
    resultados.append(tupla_plural) 

for plurales in resultados:
    print(plurales)
           
