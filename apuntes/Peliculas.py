#crear una clase llamada peliculas que contenga las siegientes propiedades
#titulo,year estreno, descripcion, clasificacion
#generar metodos get y set
#generar metodos de impresion de catalogo
#crear un objeto por cada pelicula (al menos 5 peliculas)

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
        print("-" * 40)


pelicula1 = Peliculas("Masacre en Texas", 2001, "Terror", "Adultos")
pelicula2 = Peliculas("Viernes 13", 2008, "Terror", "Adultos")
pelicula3 = Peliculas("El Hombre Araña", 2011, "Ciencia ficción", "Niños")
pelicula4 = Peliculas("Iron Man", 2022, "Ciencia ficción", "Niños")
pelicula5 = Peliculas("Hannibal Lecter", 2000, "Terror", "Adultos")

pelicula1.imprimir()
pelicula2.imprimir()
pelicula3.imprimir()
pelicula4.imprimir()
pelicula5.imprimir()
