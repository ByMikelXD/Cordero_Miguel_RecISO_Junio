'''def calificaciones():
    calificaciones = []
    for i in range(5):
        calificacion = float(input(f"Introduce la calificación del módulo {i+1}: "))
        calificaciones.append(calificacion)

    calificacion_mayor = max(calificaciones)
    calificacion_menor = min(calificaciones)
    media_calificaciones = sum(calificaciones) / len(calificaciones)

    print(f"Calificación mayor: {calificacion_mayor}")
    print(f"Calificación menor: {calificacion_menor}")
    print(f"Media de las calificaciones: {media_calificaciones:.2f}")

calificaciones()'''

'''def es_capicua():
    numero = input("Introduce un número: ")
    if numero == numero[::-1]:
        print(f"El número {numero} es capicúa.")
    else:
        print(f"El número {numero} no es capicúa.")

es_capicua()'''


def buscar_ciudad():
    ciudades = {"Madrid", "Barcelona", "Valencia", "Sevilla", "Zaragoza", "Málaga", "Murcia", "Palma", "Bilbao", "Alicante"}
    ciudad_usuario = input("Introduce el nombre de una ciudad: ").strip().capitalize()

    # Normalización de las ciudades en el conjunto
    ciudades_normalizadas = {ciudad.lower() for ciudad in ciudades}

    if ciudad_usuario.lower() in ciudades_normalizadas:
        print(f"La ciudad {ciudad_usuario} se encuentra en el conjunto.")
    else:
        print(f"La ciudad {ciudad_usuario} no se encuentra en el conjunto.")

buscar_ciudad()
