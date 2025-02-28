diccionario = {"nombre":"diego","carrera":"sis","semestre":7}
print(type(diccionario))
print('carrera' in (diccionario))
print(diccionario['carrera'])
print(diccionario.get("nombre"))
for i in diccionario.items():
    print(i)
for i in diccionario.keys():
    print(i)
for i in diccionario.values():
    print(i)
for i,j in diccionario.items():
    print(i,j)
    print(diccionario.items())
    diccionario['especialidad'] = "Aplicaciones web"
    print(diccionario)
    diccionario.pop("semestre")
    print(diccionario)