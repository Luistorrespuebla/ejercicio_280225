 print("hola mundo");
 #tipos de datos: str, float, bool, int
 entero :int = 100
 cadena :str = "luis"
 booleno :bool = True
 flotante :float 
 #interpolación
 print(f"el entero es: {entero}")
 print("cadena personalizada".center(50,"*"))
 #conocer el tipo de dato
 print(type(en
 print(f"el tipo de dato de la variable {entero} es: type({entero})".center(80,"*"))
 print(f"el tipo de dato de la variable {cadena} es: type({cadena})".center(80,"*"))
 print(f"el tipo de dato de la variable {booleno} es: type({booleno})".center(80,"*"))
 print(f"el tipo de dato de la variable {float} es: type({float})".center(80,"*"))
 #id me permite saber la direccion de memoria de una variable
 print(id(cadena))
 nombre = input("ingresa tu nombre:")
 #estructuras condicionales
 if nombre == "juan":
     print("el nombre es igual")
 elif nombre == "diego":
     print("el nombre es alberto")
 else:
     print("el nombre o es igual")