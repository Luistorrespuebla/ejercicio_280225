class Automovil:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__combustible = 100  

    def conducir(self, km=100):
        consumo = km / 10
        if self.__combustible >= consumo:
            self.__combustible -= consumo
            print(f"Has conducido {km} km. Combustible restante: {self.__combustible} litros.")
        else:
            print('Combustible bajo.')

    def recargar(self, litros=50):
        self.__combustible += litros
        self.__combustible = 100 if self.__combustible > 100 else self.__combustible 
        print(f"Has recargado: {litros} litros, ahora tienes: {self.__combustible} litros.")

    def estado(self):
        print(f"Combustible restante: {self.__combustible} litros.")
        

coche1 = Automovil("Toyota", "Yaris")
coche1.estado()
coche1.conducir()
coche1.recargar()
coche1.estado()