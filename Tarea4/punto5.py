#        ---Leer y sumar números desde un archivo---
archivo = open('datos.txt', 'r')

lineas = archivo.readlines()


suma_total = int(lineas[0]) + int(lineas[1]) + int(lineas[2])

print(f'La suma total es: {suma_total}')

archivo.close()