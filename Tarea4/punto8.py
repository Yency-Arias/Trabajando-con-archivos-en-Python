#           ---Filtrar líneas por palabra clave---

archivo = open('log.txt', 'r')

for linea in archivo:
    if 'ERROR' in linea:
        print(f'\n{linea}')

archivo.close()