import crud
from basic_functions import *


while True:
    print("Menu de opciones")
    print("1. Ver todos los registros")
    print("2. Filtrar películas")
    print("3. Agregar un registro")
    print("4. Modificar un registro")
    print("5. Eliminar")
    print("6. Salir del sistema")
    opcion = input("Ingrese un opcion: ")
    if opcion == "1":
        for movies in crud.read_peliculas():
            print("-------------------------------------------------------------------------------------------------------------")
            for key, value in movies.items():
                print(f"{key}: {value}")
        print("-------------------------------------------------------------------------------------------------------------")

    elif opcion == "2":
        wanted_key = ""
        wanted_value = ""
        op = int(input("Menú "
                   "\n1. Año de estreno"
                   "\n2. Género"
                   "\n3. Puntuación"
                   "\n4. Título de película"
                   "\n5. Por id"
                   "\nPresioné una opción:"

                   ))

        if(op ==1):
            wanted_key = "Año de estreno"
            wanted_value = input("Ingrese el año en formato: YYYY: ")

        elif (op ==2):
            wanted_key = "Género"
            wanted_value = input("Ingrese el género: ")

        elif( op ==3):
            wanted_key = "Puntuación"
            wanted_value = input("Ingrese la puntuación de 1 a 10: ")
        elif (op == 4):
            wanted_key = "Nombre"
            wanted_value = input("Ingrese la puntuación de 1 a 10: ")
        elif (op == 5):
            wanted_key = "_id"
            wanted_value = int(input("Ingrese el id: "))

        else:
            print("Ingrese un valor valido")

        movie_filter(wanted_key, wanted_value, crud.read_peliculas())

    elif opcion == "3":

        result = create_json_peliculas(int(crud.read_peliculas()[-1]["_id"]) + 1)

        crud.create_peliculas(result)

    elif opcion == "4":
        id = int(input("Ingrese el id: "))
        peliculas = create_json_update()
        crud.update(id, peliculas)

    elif opcion == "5":
        id = int(input("Ingrese el id: "))
        crud.delete(id)

    elif opcion == "6":
        break

