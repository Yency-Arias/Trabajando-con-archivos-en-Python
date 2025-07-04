#            ---Escribir datos en un archivo desde una lista---
numeros = [10, 20, 30, 40, 50]

archivo = open('numeros.txt','w')

for numero in numeros:
    archivo.write(str(numero) + '\n')

archivo.close()

print('\nArchivo creado correctamente.\n')