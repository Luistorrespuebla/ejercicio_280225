nombre = input("Ingresa tu nombre: ")

nombreSeparado=""
contador = 0
for letra in nombre:
    if contador == 0:
        nombreSeparado
    else:
        nombreSeparado+ letra
    contador += 1

print(nombreSeparado, "tu nombre tiene", contador, "letras")

