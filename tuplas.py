tupla = ('diego','juan','luis')
#print(type(tupla))
#print(tupla)
##nos permite contar cuantas veces existe un valor en la tupla
#print(tupla.count('diego'))
##permite conocer la posicion de un valor en especifico
#print(tupla.index('juan'))
#print(tupla[2])
lista_tupla = list()
for i in tupla:
    lista_tupla.append(i)
print(type(lista_tupla))
print(lista_tupla)
lista_tupla[3]="mario"
print(lista_tupla)
lista_tupla=tuple(lista_tupla)
print(type(lista_tupla))
print(lista_tupla)


    
    
