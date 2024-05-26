def representacion_numerica():
    while True:
        numero = int(input("Introduce un número del 1 al 50: "))
        if 1 <= numero <= 50:
            break
        else:
            print("Número fuera de rango. Inténtalo de nuevo.")
    
    binario = bin(numero)[2:]  # Eliminamos el prefijo '0b'
    octal = oct(numero)[2:]    # Eliminamos el prefijo '0o'
    hexadecimal = hex(numero)[2:]  # Eliminamos el prefijo '0x'
    
    print(f"Representación binaria: {binario}")
    print(f"Representación octal: {octal}")
    print(f"Representación hexadecimal: {hexadecimal}")

representacion_numerica()

'''def descomponer_dinero():
    while True:
        cantidad = int(input("Introduce una cantidad de dinero (múltiplo de 5 y máximo 3000): "))
        if cantidad % 5 == 0 and cantidad <= 3000:
            break
        else:
            print("Cantidad no válida. Inténtalo de nuevo.")
    
    billetes = [100, 50, 20, 10, 5]
    descomposicion = {}
    
    for billete in billetes:
        descomposicion[billete] = cantidad // billete
        cantidad %= billete
    
    print("Descomposición en billetes:")
    for billete, cantidad in descomposicion.items():
        if cantidad > 0:
            print(f"Billetes de {billete}: {cantidad}")

descomponer_dinero()'''

'''def calcular_area_cuadrado():
    lado = float(input("Introduce el lado del cuadrado: "))
    area = lado * lado
    print(f"El área del cuadrado es: {area:.2f}")

def calcular_area_perimetro_circulo():
    import math
    radio = float(input("Introduce el radio del círculo: "))
    area = math.pi * (radio ** 2)
    perimetro = 2 * math.pi * radio
    print(f"El área del círculo es: {area:.2f}")
    print(f"El perímetro del círculo es: {perimetro:.2f}")

def elegir_calculo():
    while True:
        opcion = input("¿Quieres calcular el área de un cuadrado o un círculo? (cuadrado/círculo): ").strip().lower()
        if opcion == "cuadrado":
            calcular_area_cuadrado()
            break
        elif opcion == "círculo" or opcion == "circulo":
            calcular_area_perimetro_circulo()
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

elegir_calculo()'''
