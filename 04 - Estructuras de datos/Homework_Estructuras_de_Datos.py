# HOMEWORK DE ESTRUCTURAS DE DATOS # ___________________________________________
# 1. Crear una lista que contenga nombres de ciudades del mundo. La lista debe 
# contener más de 5 elementos
cities = ['Caracas', 'Londres', 'Cairns', 'Valencia', 'Tokio']
#-------------------------------------------------------------------------------
# 2. Imprimir en pantalla el segundo elemento de la lista
print(cities[1])
#-------------------------------------------------------------------------------
# 3. Imprimir en pantalla del segundo al cuarto elements
print(cities[1:4])
#-------------------------------------------------------------------------------
# 4. Visualizar el tipo de dato de la lista
print(type(cities))
#-------------------------------------------------------------------------------
# 5. Visualizar todos los elementos de la lista a partir del tercero de manera
#    genérica, es decir, sin colocar de forma explícita la posición del último
#    elemento
print(cities[2:])
#-------------------------------------------------------------------------------
# 6. Visualizar los primeros 4 elementos de la lista
print(cities[:4])
#-------------------------------------------------------------------------------
# 7. Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún
#    tipo de error?
cities.append('Caracas')
cities.append('LA')
print(cities)
# No arroja ningún error
#-------------------------------------------------------------------------------
# 8. Agregar otra ciudad pero en la cuarta posición
cities.insert(3, 'Osaka')
print(cities)
#-------------------------------------------------------------------------------
# 9. Concatenar otra lista a la ya creada
cities.extend(['París', 'Seúl'])
print(cities)
#-------------------------------------------------------------------------------
# 10. Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada.
# ¿Se nota alguna particularidad?
print(cities.index('Caracas'))
# Retorna el índice de la primera coincidencia
#-------------------------------------------------------------------------------
# 11. ¿Qué pasa si se busca un elemento que no existe?
# print(cities.index(8)) 
print('...')
# Detiene la ejecución del código y arroja un error
#-------------------------------------------------------------------------------
# 12. Eliminar un elemento d ela lista
cities.remove('LA')
print(cities)
#-------------------------------------------------------------------------------
# 13. ¿Qué pasa si el elemento a eliminar no existe?
#cities.remove(8)
print(cities)
# Detiene la ejecución del código en esa línea y arroja un error
#-------------------------------------------------------------------------------
# 14. Extraer el úlimo elemento de la lista, guardarlo en una variable e
# imprimirlo
last_element = cities.pop()
print(cities, last_element)
#-------------------------------------------------------------------------------
# 15. Mostrar la lista multiplicada por 4
print(cities * 4)
#-------------------------------------------------------------------------------
# 16. Crear una tupla que contenga los números enteros del 1 al 20
my_tuple = tuple(range(1, 21))
print(my_tuple)
#-------------------------------------------------------------------------------
# 17. Imprimir desde en índice 10 al 15 de la tupla
print(my_tuple[10:16])
#-------------------------------------------------------------------------------
# 18. Evaluar si los números 20 y 30 están dentro de la tupla
print(20 in my_tuple)
print(30 in my_tuple)
#-------------------------------------------------------------------------------
# 19. Con la lista creada en el punto 1, validar la existencia del elemento
# 'París' y si no existe, agregarlo. Utilizar una variable e informar lo 
# sucedido
if ('París' in cities):
    print('La ciudad ya se encuentra almacenada')
else:
    print('La ciudad no se encuentra almacenada')
    cities.append('París')
print(cities)
#-------------------------------------------------------------------------------
# 20. Mostrar la cantidad de veces que se encuentra un elemento específico
# dentro de la tupla y de la lista
print(cities.count('Caracas'))
print(my_tuple.count(8))
#-------------------------------------------------------------------------------
# 21. convertir la tupla en una lista
print(list(my_tuple))
print(my_tuple)
# No modifica la tupla original, es necesario almacenarlo en una variable.
# únicamente se pasa el valor de la tupla como argumento de la función
# (no se pasa por referencia)
#-------------------------------------------------------------------------------
# 22. Desempaquetar sólo los primeros 3 elementos de la tupla en tres variables
first, second, third = my_tuple[:3]
print(my_tuple[:3])
print(first)
print(second)
print(third)
# Son validas las siguientes dos formas de desempaquetar:
nombre1, apellido1 = 'Ligia', 'Jorge'
nombre2, apellido2 = 'Lilibeth', 'Jorge'
print('Hola, ' + nombre1 + ' ' + apellido1)
print('Hola, ' + nombre2 + ' ' + apellido2)
#-------------------------------------------------------------------------------
# 23. Crear un diccionario utilizando la lista creada en el punto 1,
# asignandole la clave "ciudad". Agregar también otras claves, como puede ser
# "país" y "continente"
my_dictionary = {
    'cities': cities,
    'numbers': my_tuple
}
print(my_dictionary)
#-------------------------------------------------------------------------------
# 24. Imprimir las claves del diccionario
print(my_dictionary.keys())
for i in my_dictionary.keys():
    print(i)
#-------------------------------------------------------------------------------
# 25. Imprimir las ciudades a través de su clave
print(my_dictionary['cities'])
#_______________________________________________________________________________
