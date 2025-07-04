#     ---Actualizar un archivo de texto sin borrar contenido previo---

nota = input("\nEscribe una nota: ")


archivo = open('notas.txt', 'a')
archivo.write(nota + '\n')


print('\nNota creada exitosamente.')

archivo.close()