# -*- coding: utf-8 -*-
from typing import List, Dict, Set
from utils.utils import one_shot_encoding, vectorize, normalize, distance
from utils.aplicacion import Aplicacion
from kd_tree.KD_Tree import KD_Tree, KD_Node
import sys

# Declaracion de Constantes
ARCHIVO = 'datos.csv'

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
        lista_ids.append(Aplicacion(linea[1], linea[2],linea[3],
        linea[5], linea[8], linea[10], linea[11],
        linea[12], linea[15]))

    # Se obtiene una Lista Normalizada de np.arrays
    lista_vectores = normalize(lista_vectores)

    # Ciclo para insertar los vectores normalizados al kd_tree
    for i in range(len(lista_vectores)):
        lista_ids[i].vector = lista_vectores[i]
        kd_tree.insert(lista_vectores[i], lista_ids[i])


    kd_tree.k_nearest(1,lista_vectores[0])