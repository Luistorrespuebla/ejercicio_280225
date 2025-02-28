def datosGrupo():
    grupo = input('Ingresa el nombre del grupo: ')
    semestre = input('Ingresa el semestre del grupo: ')

    cantidadHorarios = int(input('Cuantos dias vas a dar de alta: '))
    horarios = []
    for i in range(cantidadHorarios):
        horario = input(f'Ingresa el horario {i+1}: ')
        horarios.append(horario)

    return grupo, semestre, horarios

def listaNombres():
    cantidad = int(input('Ingresa cuántos alumnos vas a registrar: '))
    nombres = []
    for i in range(cantidad):
        nombre = input(f'Ingresa el nombre del alumno {i+1}: ')
        nombres.append(nombre)
    return nombres

def imprimirDatos(grupo, semestre, horarios, alumnos):
    print(f"\nEl grupo: {grupo}")
    print(f"Pertenece al semestre: {semestre}")
    
    print("\nHorarios del grupo:")
    for horario in horarios:
        print(f"- {horario}")
    
    print(f"\nHas registrado {len(alumnos)} alumnos.")
    print("Lista de alumnos:")
    for alumno in alumnos:
        print(f"- {alumno}")

grupo, semestre, horarios = datosGrupo()
alumnos = listaNombres()
imprimirDatos(grupo, semestre, horarios, alumnos)
