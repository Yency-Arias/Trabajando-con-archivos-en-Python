#            ---Contar palabras de un archivo de texto---

archivo = open('frases.txt')

contenido = archivo.read()


palabras = contenido.split()
cantidad = len(palabras)


print(f'\nLas frases tienen {cantidad} palabras')

archivo.close()