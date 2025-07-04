#          ---Copiar contenido de un archivo a otro---

archivo_origen = open('origen.txt')
contenido = archivo_origen.read()

archivo_origen.close()



archivo_copia = open('copia.txt','w')
archivo_copia.write(contenido)

archivo_copia.close()

print('\nArchivo copiado correctamtente.\n')