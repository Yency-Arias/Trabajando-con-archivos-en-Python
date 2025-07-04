#        ---Contar cuántas líneas tiene un archivo---
archivo = open('poema.txt', 'r')

lineas = archivo.readlines()
cantidad = len(lineas)        

archivo.close()

print(f'El archivo contiene {cantidad} lineas.')