def funcion(nombre) -> str:
    print(f"hola mundo {nombre}")
funcion("diego")

def funcion1(*apellido:str):
    return apellido
print(f"hola mundo {funcion1("mario","saul","pinocho")}")


def funcion2(grupo,*nombre1):
    return 