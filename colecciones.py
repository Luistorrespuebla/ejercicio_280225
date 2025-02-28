#colecciones set
coleccion = {'pizza', 'tacos', 'tamales', 'hamburguesa'}
print(type(coleccion))
print(coleccion)
coleccion.add('torta')
print(coleccion)
#las colecciones no permiten la duplicidad de datos dentro de la misma
#no posee un orden especifico, por tal motivo te va a mostrar los datos de forma aleatoria
#coleccion.clear()
#elimina el valor de la coleccion
coleccion.discard('torta')
print('coleccion')