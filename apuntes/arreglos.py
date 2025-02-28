#una lista es basicamente un arreglo
lista = [1,2,3,4,5]
print(lista)
print(type(lista))
#agrega un valos mas a la lista
lista.append(6)
print(lista)
#sustitulle el valor de una posicion
lista.insert(1,10)
print(lista)
#remueve el valor de la posicion proporcionada
lista.remove(1)
print(lista)
#elimina el ultimo valor de la lista
lista.pop()
print(lista)
#elimina una posicion dada
del lista[2]
print(lista)
#limpia la lista por completo
lista.clear()
print(lista)
#eliminar lista
del lista
