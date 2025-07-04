#             ---Leer archivo CSV y mostrar contenido---
archivo = open('estudiantes.csv', 'r')
lineas = archivo.readlines()

linea1 = lineas[1].strip().split(',')

linea2 = lineas[2].strip().split(',')

linea3 = lineas[3].strip().split(',')


print(f'\n{linea1[0]} tiene {linea1[1]} años y obtuvo una calificacion de {linea1[2]}.')

print(f'{linea2[0]} tiene {linea2[1]} años y obtuvo una calificacion de {linea2[2]}.')

print(f'{linea3[0]} tiene {linea3[1]} años y obtuvo una calificacion de {linea3[2]}.')

archivo.close()