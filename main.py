# -*- coding: utf-8 -*-
from typing import List, Dict, Set
from utils.utils import one_shot_encoding, vectorize, normalize, normalize_excluded, distance, cls, menu
from utils.aplicacion import Aplicacion
from kd_tree.KD_Tree import KD_Tree, KD_Node
import copy
import sys

# Declaracion de Constantes
ARCHIVO = 'datos.csv'

def opcion_uno():
    '''
        Funcion que define el comportamiento de la primera opcion del menu.

        Solicita un Id de aplicacion, y en caso de encontrar una aplicacion
        con el id asociado la muestra por pantalla.
    '''
    # Se limpia la consola
    cls()
    # Se solicita el id a buscar
    id = input('Ingrese el id de una aplicacion a buscar : ')
    # Se obtiene la aplicacion o None
    aplicacion = diccionario_aplicaciones.get(id,None)

    if aplicacion is not None:
        print(aplicacion)
    else:
        print('No existe una aplicacion con tal id en la base de datos.')

    id = input('Presione Enter para continuar.')

def opcion_dos():
    '''
        Funcion que define el comportamiento de la segunda opcion del menu.

        Solicita un Id de aplicacion, y en caso de encontrar una aplicacion
        con el id asociado muestra sus 10 vecinos mas cercanos segun la busqueda
        KNN del KD_Tree.
    '''
    # Se limpia la consola
    cls()
    # Se solicita el id a buscar
    id = input('Ingrese el id de una aplicacion a buscar : ')
    # Se obtiene la aplicacion o None
    aplicacion = diccionario_aplicaciones.get(id,None)

    if aplicacion is not None:
        try:
            vecinos = kd_tree.k_nearest(10, aplicacion.vector, aplicacion.id)
            # Se muestran los 10 vecinos mas cercanos
            for i in range(len(vecinos)):
                cls()
                aplicacion = vecinos[i][1]
                print(f"Mostrando vecino numero {i+1}")
                print(aplicacion[0])
                inpt = input('Presione Enter para ver el siguiente vecino.')
        except:
            print('La aplicacion no cuenta con 10 vecinos (?) F')
    else:
        print('No existe una aplicacion con tal id en la base de datos.')

    id = input('Presione Enter para continuar.')


def opcion_tres():
    '''
        Funcion que define el comportamiento de la opcion 3.

        Para ello se solicitan valores para construir un vector de caracteristicas.
        Luego el vector se normaliza.
        Finalmente se aplica KNN al vector normalizado
    '''
    cls()
    tamano_bytes = int(input("Ingrese el tamano en bytes de su aplicativo : "))
    precio = float(input("Ingrese el precio en dolares de su aplicativo : "))
    user_rating = float(input("Ingrese el user rating de su aplicativo (Ej : 4.5) : "))
    cls()
    print("Opciones de Content Rating : ")
    # Se despliegan las opciones de Content Rating
    cont = 0
    for i in diccionario_content_rating.keys():
        cont = cont + 1
        print(f"{cont}) {i}")
    cont_rating = int(input("Ingrese el content rating segun la opcion del menu : "))
    cls()
    print("Opciones de Genero : ")
    # Se despliegan las opciones de Generos
    cont = 0
    for i in diccionario_generos_codificados.keys():
        cont = cont + 1
        print(f"{cont}) {i}")
    genero = int(input("Ingrese el genero segun la opcion del menu : "))

    # Se obtiene el content rating a partir de la opcion ingresada
    cont_rating = diccionario_content_rating[list(diccionario_content_rating.keys())[cont_rating-1]]
    # Se obtiene el genero a partir de la opcion ingresada
    genero = diccionario_generos_codificados[list(diccionario_generos_codificados.keys())[genero-1]]

    # Se construye el vector de caracteristicas
    vector = vectorize(tamano_bytes, precio, user_rating, cont_rating, genero)
    # Se normaliza el vector de caracteristicas
    vector = normalize_excluded(lista_vectores_no_normalizados, vector)
    # Se apica KNN al vector para obtener los 10 vecinos mas cercanos
    vecinos = kd_tree.k_nearest(10, vector, None)
    # Se muestran los 10 vecinos mas cercanos
    for i in range(len(vecinos)):
        cls()
        aplicacion = vecinos[i][1]
        print(f"Mostrando vecino numero {i+1}")
        print(aplicacion[0])
        inpt = input('Presione Enter para ver el siguiente vecino.')

    inpt = input("Presione Enter para continuar.")


if __name__ == "__main__":

    # Se hace la lectura del archivo
    archivo_datos = open(ARCHIVO, 'r', encoding='utf8')
    # Conjunto de Generos
    conjunto_generos : Set = set()
    # Conjunto de Content Ratings
    conjunto_content_rating : Set = set()
    # Skip a la primera linea
    archivo_datos.readline()
    '''
        Se hace un procesamiento inicial del texto para generar:
            - Diccionario con ID:Trackname
            - Conjunto de Generos
            - Conjunto de Content Rating
    '''
    for linea in archivo_datos:
        '''
            0 : Numeral
            1 : Id
            2 : Track Name
            3 : size_bytes
            4 : currency
            5 : price
            6 : rating_count_tot
            7 : rating_count_ver
            8 : user_rating
            9 : user_rating_ver
            10 : ver
            11 : cont_rating
            12 : prime_genre
            13 : sup_devices.num
            14 : ipadSc_urls.num
            15 : lang.num
            16 : vpp_lic
        '''
        linea = linea.strip().split(',')
        # Se agrega el genero a un conjunto
        conjunto_generos.add(linea[12])
        # Se agrega el content rating a un conjunto
        conjunto_content_rating.add(linea[11])
    # Se obtiene un diccionario de Generos Codificados con OneShot Encoding
    diccionario_generos_codificados = one_shot_encoding(conjunto_generos)
    # Se obtiene un dicciionario de Content Rating codificados con OneShot Encoding
    diccionario_content_rating = one_shot_encoding(conjunto_content_rating)
    # Se hace un rewind al archivo.
    archivo_datos.seek(0)
    # Skip primera linea
    archivo_datos.readline()
    # Conjunto de vectores
    lista_vectores : List = list()
    # Lista de Aplicaciones
    lista_ids : List = list()
    # Se crea el KD_Tree
    kd_tree = KD_Tree()
    # Diccionario de Aplicaciones
    diccionario_aplicaciones : Dict = dict()
    for linea in archivo_datos:
        '''
            0 : Numeral
            1 : Id
            2 : Track Name
            3 : size_bytes
            4 : currency
            5 : price
            6 : rating_count_tot
            7 : rating_count_ver
            8 : user_rating
            9 : user_rating_ver
            10 : ver
            11 : cont_rating
            12 : prime_genre
            13 : sup_devices.num
            14 : ipadSc_urls.num
            15 : lang.num
            16 : vpp_lic
        '''
        linea = linea.strip().split(',')
        # Se obtiene el vector utilizando la funcion vectorize definida en utils.py
        vector = vectorize(linea[3], linea[5], linea[8], 
                        diccionario_content_rating.get(linea[11]),
                        diccionario_generos_codificados.get(linea[12]))
        lista_vectores.append(vector)
        aplicacion =  Aplicacion(linea[1], linea[2],linea[3],
        linea[5], linea[8], linea[10], linea[11],
        linea[12], linea[15])
        lista_ids.append(aplicacion)
        diccionario_aplicaciones[linea[1]] = aplicacion

    # Se obtiene una Lista Normalizada de np.arrays
    lista_vectores_no_normalizados = copy.deepcopy(lista_vectores)
    lista_vectores = normalize(lista_vectores)

    # Ciclo para insertar los vectores normalizados al kd_tree
    for i in range(len(lista_vectores)):
        lista_ids[i].vector = lista_vectores[i]
        kd_tree.insert(lista_vectores[i], lista_ids[i])


    while True:
        menu()
        #print(diccionario_aplicaciones)
        opcion = input("Ingrese su opcion deseada : ")

        if opcion == '1':
            opcion_uno()
        elif opcion == '2':
            opcion_dos()
        elif opcion == '3':
            opcion_tres()
        else:
            print('Adios <3')
            sys.exit(-1)

    #kd_tree.k_nearest(5,lista_vectores[10])


