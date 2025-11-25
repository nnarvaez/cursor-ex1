opcion = ""
while opcion != "Salir":
    print("Calculadora, ingrese opción")
    print("Sumar")
    print("Restar")
    print("Multiplicar")
    print("Dividir")
    print("Salir")
    opcion = input("Ingrese una opción: ")
    
    if opcion != "Salir":
        try:
            numero1 = int(input("Ingrese el primer número: "))
            numero2 = int(input("Ingrese el segundo número: "))
            
            match opcion:
                case "Sumar":
                    print("Sumar", numero1 + numero2)
                case "Restar":
                    print("Restar", numero1 - numero2)
                case "Multiplicar":
                    print("Multiplicar", numero1 * numero2)
                case "Dividir":
                    if numero2 != 0:
                        print("Dividir", numero1 / numero2)
                    else:
                        print("Error: División por cero")
                case _:
                    print("Opción inválida")
        except ValueError:
            print("Error: Debes ingresar números enteros válidos")
