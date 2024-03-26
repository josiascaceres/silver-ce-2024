"""
Este es el solucionario del ejercitario de manipulacion de Strings de la UNI. Ante cualquier consulta:
"""

#1
"""
nombre = 'Juan'
entero = 4

repeticion = nombre * entero

print(repeticion)"""

#2
"""
nombre = 'Juan'
apellido = 'Arias'

nombre_apellido = nombre + ' ' + apellido

veces = 10

print((nombre_apellido + '\n') * veces)
"""

#3
"""
nombre = 'Samuel'
apellido = 'Caceres'

nombre_completo = nombre + ' ' + apellido
nombre_completo_sin_espacio = nombre + apellido

n = len(nombre_completo_sin_espacio)

print(nombre_completo + ' tiene ' + str(n) + " letras.")
"""

#4
"""
#Asignar los valores a la variable
producto = 'Manzana'
cantidad = 10
precio_unitario = 5000

#Calcular precio total
precio_total = precio_unitario * cantidad

#Convertir valores a STR
precio_unitario_str = str(precio_unitario)
cantidad_str = str(cantidad)
precio_total_str = str(precio_total)

#sacar la longitud de los valores en STR
long_precio_unitario_str = len(precio_unitario_str)
long_cantidad_str = len(cantidad_str)
long_precio_total_str = len(precio_total_str)

#agregamos los 0 faltantes a los valores
ceros_precio_unitario = 6 - long_precio_unitario_str
precio_unitario_final = ('0' * ceros_precio_unitario) + precio_unitario_str

ceros_cantidad = 3 - long_cantidad_str
cantidad_final = ('0' * ceros_cantidad) + cantidad_str

ceros_precio_total = 8 - long_precio_total_str
precio_total_final = ('0' * ceros_precio_total) + precio_total_str

#Guardar en una variable el caracter guion
guion = '_'

#Hacemos el print final
print(producto + guion + precio_unitario_final + guion + cantidad_final + guion + precio_total_final)

"""

#5
"""
frase = 'hola mundo'
vocal = 'z'

vocal = vocal.upper()

frase += vocal

print(frase)
"""

#6
"""
texto = 'Hola mundo'
n = 5

print((texto + ' ') * n)
"""

#7
"""
libro = 'harry potter'

libro_sin_espacios = libro.replace(' ' , '')

cantidad_caracteres = len(libro_sin_espacios)

print('El libro ' + libro.title() + ' tiene ' + str(cantidad_caracteres) + ' letras.')"""
