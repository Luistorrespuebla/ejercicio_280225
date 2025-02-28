class Peliculas:
    def __init__(self, titulo, year_estreno, descripcion, clasificacion):
        self.__titulo = titulo
        self.__year_estreno = year_estreno
        self.__descripcion = descripcion
        self.__clasificacion = clasificacion

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def year_estreno(self):
        return self.__year_estreno

    @year_estreno.setter
    def year_estreno(self, year_estreno):
        self.__year_estreno = year_estreno

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion

    @property
    def clasificacion(self):
        return self.__clasificacion

    @clasificacion.setter
    def clasificacion(self, clasificacion):
        self.__clasificacion = clasificacion

    def imprimir(self):
        print(f"Título: {self.__titulo}")
        print(f"Año de estreno: {self.__year_estreno}")
        print(f"Descripción: {self.__descripcion}")
        print(f"Clasificación: {self.__clasificacion}")
        print("*" * 20)


class CatalogoPeliculas:
    def __init__(self):
        self.peliculas = []

    def agregar_pelicula(self):
        titulo = input("Ingrese el título de la película: ")
        year_estreno = input("Ingrese el año de estreno: ")
        descripcion = input("Ingrese la descripción: ")
        clasificacion = input("Ingrese la clasificación: ")

        nueva_pelicula = Peliculas(titulo, year_estreno, descripcion, clasificacion)
        self.peliculas.append(nueva_pelicula)
        print(f"Operación exitosa.")

    def listar_peliculas(self):
        if not self.peliculas:
            print("El catálogo está vacío.")
            return

        for idx, pelicula in enumerate(self.peliculas, start=1):
            print(f"[{idx}] {pelicula.titulo}")
            pelicula.imprimir()

    def editar_pelicula(self, indice):
        if 0 <= indice < len(self.peliculas):
            pelicula = self.peliculas[indice]
            pelicula.imprimir()
            pelicula.titulo = input("Nuevo título: ") or pelicula.titulo
            pelicula.year_estreno = input("Nuevo año de estreno: ") or pelicula.year_estreno
            pelicula.descripcion = input("Nueva descripción: ") or pelicula.descripcion
            pelicula.clasificacion = input("Nueva clasificación: ") or pelicula.clasificacion
        else:
            print("No existe esa opción.")

    def eliminar_pelicula(self, indice):
        if 0 <= indice < len(self.peliculas):
            print(f"Película '{self.peliculas[indice].titulo}' eliminada.")
            del self.peliculas[indice]
        else:
            print("No existe esa opción.")


catalogo = CatalogoPeliculas()

while True:
    print("\n1) Listado de películas")
    print("2) Editar película")
    print("3) Eliminar película")
    print("4) Salir")
    print("5) Agregar película")  
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        catalogo.listar_peliculas()
    elif opcion == "2":
        indice = int(input("Ingrese el número de la película a editar: ")) - 1
        catalogo.editar_pelicula(indice)
    elif opcion == "3":
        indice = int(input("Ingrese el número de la película a eliminar: ")) - 1
        catalogo.eliminar_pelicula(indice)
    elif opcion == "4":
        print("Vuelva pronto.")
        break
    elif opcion == "5":
        catalogo.agregar_pelicula()  
    else:
        print("No existe esa opción.")
