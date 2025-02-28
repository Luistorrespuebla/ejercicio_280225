class CuentaBancaria:
    def __init__(self, titular):
        self.__titular = titular  
        self.__saldo = 0  

    def depositar(self, cantidad):
        self.__saldo += cantidad
        print(f"Depósito de {cantidad} realizado. Saldo actual: {self.__saldo}")

    def retirar(self, cantidad):
        self.__saldo = self.__saldo - cantidad if self.__saldo >= cantidad else self.__saldo 
        print(f"Retiro de {cantidad} realizado." if self.__saldo >= cantidad else "Saldo insuficiente.")
        print(f"Saldo actual: {self.__saldo}")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.__saldo}")

titular = input("Ingrese el nombre del titular de la cuenta: ")
cuenta = CuentaBancaria(titular)

while True:
    print("\nOpciones:")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Mostrar saldo")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cantidad = float(input("Ingresa la cantidad a depositar: "))
        cuenta.depositar(cantidad)
    elif opcion == "2":
        cantidad = float(input("Ingresa la cantidad a retirar: "))
        cuenta.retirar(cantidad)
    elif opcion == "3":
        cuenta.mostrar_saldo()
    elif opcion == "4":
        break
    else:
        print("No contamos con esa opción en BBVA.")