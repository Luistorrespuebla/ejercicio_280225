class Persona: 
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

persona1 = Persona ("luis","torres",30,"m")
print(type(persona1))
#persona1.mostrar()
#persona1.mostrarNombre()
#persona1.mostrarApellido()
#persona1.mostrarEdad()
#persona1.mostrarSexo()
persona1.__nombre="alberto"
#persona1.mostrar()
persona1.__apellido="zorra"
#persona1.mostrar()    
persona1.mostrar2
#self es  el equivalente a this