from misConstantes import NOMBRE

class Persona: 
    
    CONSTANTE=3 #para declarar una constante siempre es en mayusculas
    
    def __init__(self,nombre,apellido,edad,sexo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__sexo = sexo
        self.__mostrar2()
    @property #decorador 
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    
    @property    
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self,apellido):
        self.__apellido = apellido
        
    @property    
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self,edad):
        self.__edad = edad
        
    @property    
    def sexo(self):
        return self.__sexo
    
    @sexo.setter
    def sexo(self,sexo):
        self.__sexo = sexo

    def mostrar(self):
        print(f"Datos: nombre: {self.__nombre}, apellido: {self.__apellido}, edad: {self.__edad}, sexo: {self.__sexo}")
    
    def mostrar2(self):
        print(f"Datos: nombre: {self.__nombre}, apellido: {self.__apellido}, edad: {self.__edad}, sexo: {self.__sexo}")

    @staticmethod
    def mostrar_variables():
        print(Persona.apellido)

    #los metodos estaticos son accesos rapidos ya que no se necesita instanciar la clase
    #accede mediente una instancia de clase, mientras que el otro entra mediante una instancia de objeto

    @classmethod
    def leer_contenido(cls):
        print(cls.nombre)
    
    
    
