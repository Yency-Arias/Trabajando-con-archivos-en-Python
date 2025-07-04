#             ---Lectura de lineas de un archivo de texto---

archivo = open('nombres.txt')

contenido = archivo.read()

print(contenido)


archivo.close()