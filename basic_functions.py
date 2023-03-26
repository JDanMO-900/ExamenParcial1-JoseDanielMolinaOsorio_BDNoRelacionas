def create_json_peliculas(id):

    nombre = input("Nombre: ")
    anio = input("Año de Lanzamiento: ")
    genero = input("Genero: ")
    puntuacion = input("Puntuación: ")
    review = input("Crítica: ")
    sinopsis = input("Sinopsis: ")
    director = input("Director: ")
    reparto = input("Reparto: ")

    peliculas = {
        "_id": id,
        "Nombre": nombre,
        "Año de estreno": anio,
        "Género": genero,
        "puntuación": puntuacion,
        "Crítica": review,
        "Sinopsis": sinopsis,
        "Director": director,
        "Reparto": reparto
    }

    return peliculas


def create_json_update():
    print("Menu de opciones\n"
          "1. Modificar todos los datos del documento\n"
          "2. Modificar un elemento del documento")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        nombre = input("Nombre: ")
        anio = input("Año de Lanzamiento: ")
        genero = input("Genero: ")
        puntuacion = input("Puntuación: ")
        review = input("Crítica: ")
        sinopsis = input("Sinopsis: ")
        director = input("Director: ")
        reparto = input("Reparto: ")

        peliculas = {"Nombre": nombre,
                     "Año de estreno": anio,
                     "Género": genero,
                     "puntuación": puntuacion,
                     "Crítica": review,
                     "Sinopsis": sinopsis,
                     "Director": director,
                     "Reparto": reparto}
        return peliculas

    elif opcion == "2":
        indice = ""
        op = int(input("1. Nombre"
              "\n2. Año de estreno"
              "\n3. Género"
              "\n4. puntuación"
              "\n5. Crítica"
              "\n6. Sinopsis"
              "\n7. Director"
              "\n8. Reparto"
             "\n Ingrese una opción"))

        if op == 1:
            indice = "Nombre"
        elif op == 2:
            indice = "Año de estreno"
        elif op == 3:
            indice = "Género"
        elif op == 4:
            indice = "puntuación"
        elif op == 5:
            indice = "Crítica"
        elif op == 6:
            indice = "Sinopsis"
        elif op == 7:
            indice = "Director"
        elif op == 8:
            indice = "Reparto"

        print(indice)
        valor = input("Ingrese el valor a modificar: ")
        peliculas = {indice: valor}
        return peliculas


def movie_filter(wanted_key, wanted_value, dictionaries):
    print(
        "-------------------------------------------------------------------------------------------------------------")
    for i in range(len(dictionaries)):

        for (key, value) in dictionaries[i].items():

            if key == wanted_key and value == wanted_value:
                for (key1, value1) in dictionaries[i].items():
                    print(key1, value1)
    print(
        "-------------------------------------------------------------------------------------------------------------")


