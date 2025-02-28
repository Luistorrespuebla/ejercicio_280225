from CONSTANTE import N1, N2, N3, K  

class Opciones:
    
    def fahrenheit_a_celsius(self, grados=0):
        print(f'°C = ({grados} °F - {N1}) × {N2}')
        print(f'°C = {(grados - N1) * N2}')
    
    def celsius_a_fahrenheit(self, grados=0):
        print(f'°F = ({grados} °C × {N3}) + {N1}')
        print(f'°F = {(grados * N3) + N1}')
    
    def celsius_a_kelvin(self, grados=0):
        print(f'K = {grados} °C + {K}')
        print(f'K = {grados + K}')
    
    def kelvin_a_celsius(self, grados=0):
        print(f'°C = {grados} K - {K}')
        print(f'°C = {grados - K}')

opcion = Opciones()

def menu():  
    while True:
        seleccion = input('1) Fahrenheit a Celsius\n2) Celsius a Fahrenheit\n3) Celsius a Kelvin\n4) Kelvin a Celsius\n5) Salir\nNúmero de opción: ')

        if not seleccion.isdigit():  
            print("Entrada no válida. Por favor, ingresa un número del 1 al 5.")
            continue

        seleccion = int(seleccion)

        if seleccion == 5:
            break

        g = input('Ingresa los grados: ')
        if not g.replace('.', '', 1).isdigit():  
            print("Entrada no válida. Ingresa un número válido.")
            continue

        g = float(g)  


        {
            1: lambda: opcion.fahrenheit_a_celsius(g),
            2: lambda: opcion.celsius_a_fahrenheit(g),
            3: lambda: opcion.celsius_a_kelvin(g),
            4: lambda: opcion.kelvin_a_celsius(g),
        }.get(seleccion, lambda: print("Opción no válida"))()


menu()
