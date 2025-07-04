#        ---Escribir un diccionario en formato JSON---
import json

persona = {
    'nombre': 'Carlos',
    'edad': 28,
    'ciudad': 'Santo Domingo'
}


archivo = open('persona.json', 'w')
json.dump(persona, archivo, indent=4)

print('Diccionario creado perfectamente.')

archivo.close()