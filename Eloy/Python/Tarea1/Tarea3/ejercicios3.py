'''funciones'''

import math

def leer_fraccion():
    numerador = int(input("Introduce el numerador: "))
    denominador = int(input("Introduce el denominador: "))
    if denominador == 0:
        raise ValueError("El denominador no puede ser 0.")
    return simplificar_fraccion(numerador, denominador)

def escribir_fraccion(numerador, denominador):
    if denominador == 1:
        print(f"{numerador}")
    else:
        print(f"{numerador}/{denominador}")

def calcular_mcd(a, b):
    return math.gcd(a, b)

def simplificar_fraccion(numerador, denominador):
    mcd = calcular_mcd(numerador, denominador)
    return numerador // mcd, denominador // mcd

def sumar_fracciones(n1, d1, n2, d2):
    numerador = n1 * d2 + n2 * d1
    denominador = d1 * d2
    return simplificar_fraccion(numerador, denominador)

def restar_fracciones(n1, d1, n2, d2):
    numerador = n1 * d2 - n2 * d1
    denominador = d1 * d2
    return simplificar_fraccion(numerador, denominador)

def multiplicar_fracciones(n1, d1, n2, d2):
    numerador = n1 * n2
    denominador = d1 * d2
    return simplificar_fraccion(numerador, denominador)

def dividir_fracciones(n1, d1, n2, d2):
    if n2 == 0:
        raise ValueError("No se puede dividir por una fracción con numerador 0.")
    numerador = n1 * d2
    denominador = d1 * n2
    return simplificar_fraccion(numerador, denominador)



'''menu'''

def menu():
    while True:
        print("\nMenú de operaciones con fracciones:")
        print("1. Sumar dos fracciones")
        print("2. Restar dos fracciones")
        print("3. Multiplicar dos fracciones")
        print("4. Dividir dos fracciones")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '5':
            print("Saliendo del programa.")
            break
        
        try:
            print("Introduce la primera fracción:")
            n1, d1 = leer_fraccion()
            print("Introduce la segunda fracción:")
            n2, d2 = leer_fraccion()
            
            if opcion == '1':
                resultado = sumar_fracciones(n1, d1, n2, d2)
                print("Resultado de la suma:")
            elif opcion == '2':
                resultado = restar_fracciones(n1, d1, n2, d2)
                print("Resultado de la resta:")
            elif opcion == '3':
                resultado = multiplicar_fracciones(n1, d1, n2, d2)
                print("Resultado de la multiplicación:")
            elif opcion == '4':
                resultado = dividir_fracciones(n1, d1, n2, d2)
                print("Resultado de la división:")
            else:
                print("Opción no válida. Por favor, elige una opción del 1 al 5.")
                continue
            
            escribir_fraccion(*resultado)
        
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    menu()


